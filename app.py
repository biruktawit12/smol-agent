import sys
sys.path.append('./smol-agent')  # 👈 Add path to local smol-agent

from smol_agent.agent import SmolAgent  # Adjust based on smol-agent’s structure

import gradio as gr

agent = SmolAgent(...)  # Initialize with required config

def run_agent(input_text):
    return agent.run(input_text)

iface = gr.Interface(fn=run_agent, inputs="text", outputs="text")
iface.launch()
