from Website import create_app

app = create_app()

#will only work if you run the file and not if you import it 
if __name__ == '__main__':
    #runs the webserver if you run the file 
    app.run(debug=True)