class ReflectionAgent:

    def generate(self, impulse_type, context):

        reflections = {

            "Necessity": {
                "reflection":
                "The purchase appears driven by a genuine functional need. If replacement is required, consider durable and repairable options.",
                "action":
                "Check whether repair is possible before replacing the product."
            },

            "Upgrade": {
                "reflection":
                "The purchase appears motivated by improved features rather than product failure. Consider whether your current product still meets your needs.",
                "action":
                "Compare the expected benefit against extending the lifespan of your existing product."
            },

            "Emotional": {
                "reflection":
                "The purchase appears emotionally driven. Waiting a few days before purchasing may help determine whether the need is genuine.",
                "action":
                "Try a 48-hour pause before making the final purchase decision."
            },

            "Comparison": {
                "reflection":
                "The motivation appears influenced by comparison, trends, or external recommendations. Consider whether the purchase solves a real problem you currently face.",
                "action":
                "List three practical reasons you need the product beyond trends or recommendations."
            }
        }

        result = reflections.get(
            impulse_type,
            {
                "reflection":
                "Consider whether this purchase aligns with your actual needs.",
                "action":
                "Take a moment to evaluate the necessity of the purchase."
            }
        )

        return f"""
Sustainability Context:
{context[:500]}

Reflection:
{result['reflection']}

Suggested Action:
{result['action']}
"""