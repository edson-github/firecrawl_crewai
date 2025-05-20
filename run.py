from firecrawl_tool import resumir_url_com_firecrawl

url = input("Informe a URL para análise: ")
resumo = resumir_url_com_firecrawl(url)

if resumo:
    print("\nResumo do conteúdo:")
    print(resumo)
else:
    print("Não foi possível obter o conteúdo.")

