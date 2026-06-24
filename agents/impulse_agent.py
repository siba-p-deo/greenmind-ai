class ImpulseAgent:

    def classify(self, answers):

        reason = answers["reason"].lower()

        if any(word in reason for word in [
            "broken",
            "not working",
            "damaged",
            "required"
        ]):

            return {
                "impulse_type": "Necessity",
                "reasoning":
                "Detected because the user described a functional problem or product failure."
            }

        elif any(word in reason for word in [
            "better",
            "upgrade",
            "new features"
        ]):

            return {
                "impulse_type": "Upgrade",
                "reasoning":
                "Detected because the user mentioned improved features or performance rather than replacement of a failed product."
            }

        elif any(word in reason for word in [
            "sale",
            "discount",
            "wanted",
            "feel good"
        ]):

            return {
                "impulse_type": "Emotional",
                "reasoning":
                "Detected because the purchase appears influenced by emotions, promotions, or personal desire."
            }

        else:

            return {
                "impulse_type": "Comparison",
                "reasoning":
                "Detected because the purchase motivation appears driven by comparison, trends, recommendations, or preference evaluation."
            }