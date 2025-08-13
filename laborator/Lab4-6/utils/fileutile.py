def clearFileContent(fileName):
    """
    Clear the content of a file
    Post: The given file exist and is empty
    """

    file = open(fileName, "w")
    file.close()