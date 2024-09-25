from openai import OpenAI, APITimeoutError

client = OpenAI(

    #Endpoint to LM Studio.
    base_url="http://localhost:1234/v1", api_key="lm-studio")


def formular(prompt, numero):

    try:
        print(f"{prompt} {numero}")
        completion = client.chat.completions.create(

            model="model-identifier",
            messages=[
                
                {"role": "system", "content": f"Devuelves {numero} películas basadas en la petición que tenga buena puntuación y que sean más o menos conocidas, no quiero películas malas o películas que no sean muy conocidas. Cada titulo separado por coma. Cada titulo entre comillas dobles. Formato estricto sin markdown. Sin caracteres escapados. Sin punto final. Sin absolutamente nada más de lo que digo."},

                {"role": "user", "content": f"{prompt}"}
            ],
            timeout=3,
            temperature=0,
        )

    except APITimeoutError:
        return ""

    return completion.choices[0].message.content
