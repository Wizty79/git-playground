import oneai
import keys

oneai.api_key = keys.oneai_api_key

your_input = " summarize this text "

pipeline = oneai.Pipeline(steps=[
    oneai.skills.Summarize(max_length=20),
])

output = pipeline.run(your_input)

print(output.summary.text)

