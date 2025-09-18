from exec import execute

if __name__ == '__main__':
    execute("./deployment/orchestration.yaml", "somethingtostack", "deploy", "./test", 1)
