from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WaterInputSerializer
import os
import pandas as pd
import dill
import joblib

# ------------------ Load Models at Startup ------------------ #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'Saved-models', 'final_ensemble_model.pkl')
scaler_path = os.path.join(BASE_DIR, 'Saved-models', 'scaler.pkl')
columns_path = os.path.join(BASE_DIR, 'Saved-models', 'feature_columns.pkl')

try:
    with open(model_path, 'rb') as f:
        loaded_model = dill.load(f)
    print("✅ Ensemble model loaded. Type:", type(loaded_model))

    scaler = joblib.load(scaler_path)
    print("✅ Scaler loaded.")

    feature_columns = joblib.load(columns_path)
    print("✅ Feature columns loaded.")

except Exception as e:
    raise RuntimeError(f"❌ Model loading failed: {e}")

# ------------------ Interpretation Logic ------------------ #

def interpret(score):
    if score < 0.1:
        return "❌ Extremely unsafe. Water is highly contaminated and not suitable for drinking."
    elif score < 0.2:
        return "⚠️ Very high risk. Water is likely unsafe and should not be consumed without treatment."
    elif score < 0.3:
        return "⚠️ High risk. Water quality is poor and may not be safe to drink."
    elif score < 0.4:
        return "⚠️ Slightly risky. Water might be unsafe; filtration or testing is advised."
    elif score < 0.5:
        return "🟡 Uncertain. Water may not be safe; consider additional testing."
    elif score < 0.6:
        return "🟢 Possibly safe. Water seems okay but monitoring is recommended."
    elif score < 0.7:
        return "✅ Likely safe. Water meets most safety standards."
    elif score < 0.8:
        return "✅ Safe. Water is good for drinking based on current parameters."
    elif score < 0.9:
        return "💧 Very safe. Water quality is excellent."
    else:
        return "🚰 Extremely safe. Water is exceptionally clean and safe to consume."

# ------------------ API View ------------------ #

class WaterPredictAPIView(APIView):
    def get(self, request):
        return Response({"detail": "GET not allowed on this endpoint."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = WaterInputSerializer(data=request.data)
        
        if serializer.is_valid():
            data = serializer.validated_data
            input_df = pd.DataFrame([data])

            try:
                input_df = input_df[feature_columns]
                prediction = loaded_model.predict(input_df)[0]
                message = interpret(prediction)

                return Response({
                    'score': prediction,
                    'message': message
                }, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'error': 'Invalid input', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
