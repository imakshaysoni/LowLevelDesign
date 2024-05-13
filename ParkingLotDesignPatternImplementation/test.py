import datetime

loader_source_snippets = {'C:\\Users\\AkshaySoni\\akshay\\opcito\\pebblo-langchain\\samples\\medical-advice\\data\\DefibrillatorGuide.pdf': {'findings_entities': 0, 'findings_topics': 1, 'findings': 1, 'fileOwner': 'FileOwner', 'sourceSize': 553055}}
loader_details = [{'name': 'PyPDFLoader', 'sourcePath': 'C:\\Users\\AkshaySoni\\akshay\\opcito\\pebblo-langchain\\samples\\medical-advice\\data\\DefibrillatorGuide.pdf', 'sourceType': 'file', 'sourceSize': 553055, 'sourceFiles': [{'name': 'C:\\Users\\AkshaySoni\\akshay\\opcito\\pebblo-langchain\\samples\\medical-advice\\data\\DefibrillatorGuide.pdf', 'findings_entities': 0, 'findings_topics': 1, 'findings': 1}], 'lastModified': datetime.datetime(2024, 2, 7, 18, 21, 5, 938175)}]

for loader in loader_details:
    for source_file in loader.get("sourceFiles", []):
        print(source_file)
        name = source_file["name"]
        if name in loader_source_snippets:
            loader_source_snippets[name]["findings"] += source_file["findings"]
            loader_source_snippets[name]["findings_topics"] += source_file["findings_topics"]
            loader_source_snippets[name]["findings_entities"] += source_file["findings_entities"]
        else:
            loader_source_snippets[name] = source_file

    new_source_file = [{
        "name": key,
        "findings_entities": value['findings_entities'],
        "findings_topics": value['findings_topics'],
        "findings": value['findings']
    }
        for key, value in loader_source_snippets.items()
    ]

    loader["sourceFiles"] = new_source_file

print(f"LD: {loader_details}")