import os

while True:
    app_name = input("Enter App Name: ")
    if app_name.strip() != "":
        break
    print("App name cannot be empty")

while True:
    app_description = input("Enter App Description: ")
    if app_description.strip() != "":
        break
    print("Description cannot be empty")

while True:
    author_name = input("Enter Author Name: ")
    if author_name.strip() != "":
        break
    print("Author name cannot be empty")

if os.path.exists(app_name):
    print("Folder already exists")
else:
    os.mkdir(app_name)

    app_json_content = '{\n'
    app_json_content += '  "name": "' + app_name + '",\n'
    app_json_content += '  "description": "' + app_description + '",\n'
    app_json_content += '  "author": "' + author_name + '"\n'
    app_json_content += '}'

    index_ts_content = "export class App {\n"
    index_ts_content += "  constructor() {\n"
    index_ts_content += "    console.log('App initialized');\n"
    index_ts_content += "  }\n"
    index_ts_content += "}\n"

    readme_content = "# " + app_name + "\n\n"
    readme_content += app_description + "\n"

    f1 = open(app_name + "/app.json", "w")
    f1.write(app_json_content)
    f1.close()

    f2 = open(app_name + "/index.ts", "w")
    f2.write(index_ts_content)
    f2.close()

    f3 = open(app_name + "/README.md", "w")
    f3.write(readme_content)
    f3.close()

    print("Rocket.Chat app template created successfully")