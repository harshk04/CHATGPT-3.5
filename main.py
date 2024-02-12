from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'YOUR API KEY'

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get input from the user
        user_input = request.json['user_input']

        # Break the loop if the user enters 'exit'
        if user_input.lower() == 'exit':
            return jsonify({"response": "Chatbot session ended."})

        # Send the message to OpenAI's API and receive the response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        # Get the model's response content
        if completion.choices[0].message is not None:
            response = completion.choices[0].message['content']
            return jsonify({"response": response})
        else:
            return jsonify({"response": 'Failed to generate response!'})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
