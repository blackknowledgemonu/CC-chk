import time
from custom_charge import custom_charge

def main(card_data):
    start_time = time.time()
    try:
        # استدعاء البوابة الجديدة (Stripe Custom Charge)
        result = custom_charge(card_data)
    except Exception as e:
        return f"{card_data}", f"Error: {str(e)}", False, 0, "❌ Internal Error"

    return result
