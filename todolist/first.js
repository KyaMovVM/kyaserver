import ollama from 'ollama'

const response = await ollama.chat({
  model: 'gemma3',
  messages: [{ role: 'user', content: 'Why is the sky blue?' }],
})
console.log(response.message.content)

const response = await ollama.chat({
  model: 'gemma3',
  messages: [{ role: 'user', content: response.message.content}],
})

console.log(response.message.content)