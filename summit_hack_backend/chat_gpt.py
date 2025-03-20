import openai


def ask_chat_gpt(prompt, model="gpt-4"):
    api_key = ""
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": """
                You will receive a prompt related to wealth management. Your task is to break it down into multiple specific queries suitable for a stateless third-party API. Each query should be self-contained, including all necessary parameters especially the users assets and shares. Additionally, select the most suitable widget type to display the results. Answer only in the JSON format provided in the example.

                Widget Types: news, timeseries, kpi, customer
                
                Some interesting KPIs to use in queries:
                market capitalization, price to earnings, earnings to share, dividend yield, performance, volatility, sharpe ratio, beta...
                
                Example:
                 
                Prompt: "Why is Teslas stock price developing so badly?"
                
                Your Answer: [
                {
                "clean_query": "What are current events regarding tesla",
                "widget": "news" 
                },
                {
                "clean_query":  "How did the tesla stock develop over the last year?",
                "widget": "timeseries"
                },
                {
                "clean_query":  "What is the volatility of the tesla stock",
                "widget": "kpi"
                }
                ]
        """},
                  {"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=200,
    )

    return response.choices[0].message.content.strip()
