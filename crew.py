# define agent and task
from crewai import Crew, Agent, Task
from firecrawl_tool import FirecrawlTool

# Cria o agente
leitor_web = Agent(
    role="Pesquisador da Web",
    goal="Buscar e explicar o conteúdo de uma página da internet",
    backstory="Especialista em analisar páginas e extrair resumos inteligentes",
    verbose=True,
    tools=[FirecrawlTool()]
)

# Define a tarefa
def criar_tarefa(url: str):
    return Task(
        description=f"Leia e resuma o conteúdo da seguinte URL: {url}",
        expected_output="Um resumo claro e completo sobre o conteúdo da página",
        agent=leitor_web
    )

# Define a Crew
def criar_crew(url: str):
    tarefa = criar_tarefa(url)
    return Crew(agents=[leitor_web], tasks=[tarefa])
