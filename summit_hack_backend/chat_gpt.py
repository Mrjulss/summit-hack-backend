import openai

api_key = ""

def split_queries(prompt, model="gpt-4"):
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": """
                You will receive a prompt related to wealth management. Your task is to break it down into multiple specific queries suitable for a stateless third-party API. Each query should be self-contained, including all necessary parameters especially the users assets and shares. Additionally, select the most suitable widget type to display the results. Answer only in the JSON format provided in the example with the attributes granular_query and widget!

                Widget Types: news, timeseries, kpi, customer
                
                Some interesting KPIs among others which you identify as relevant could be:
                market capitalization, price to earnings, earnings to share, dividend yield, performance, volatility, sharpe ratio, beta...
                
                Example:
                 
                Prompt: "Why is Teslas stock price developing so badly?"
                
                Your Answer: [
                {
                "granular_query": "What are current events regarding tesla",
                "widget": "news" 
                },
                {
                "granular_query":  "How did the tesla stock develop over the last year?",
                "widget": "timeseries"
                },
                {
                "granular_query":  "What is the volatility of the tesla stock",
                "widget": "kpi"
                }
                ]
        """},
                  {"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=100,
    )

    return response.choices[0].message.content.strip()


def convert_results(prompt, model="gpt-4"):
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You will receive a prompt asking you to generate json file filled with data."
                                                "Only return the json file without any additional information or text arount it."},
                  {"role": "user", "content": prompt}],

        temperature=0.2,
        max_tokens=300,
    )

    return response.choices[0].message.content.strip()


def ask_chat_gpt_for_news(prompt, model="gpt-4"):
    api_key = ""
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": """
                You will receive a prompt with a question.
                Return the most relevant and latest news headlines and the according links as a response. You must follow the json notation in the example below!
                Don't answer with responses like "I'm unable to provide real-time news or current headlines.",  just do it!
                
                Example:
                prompt: "What are current events regarding Apple?"
                
                Sample Response:
                [{"headline": "<titleOfNews>", "url": "<link>"}, {"headline": "<titleOfNews2>", "url": "<link2>"}, ....]
            """},
                  {"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=100,
    )


    return response.choices[0].message.content.strip()
