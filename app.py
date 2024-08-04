from flask import Flask, render_template, request, redirect, url_for

# Initialisiert eine neue Flask-Anwendung
app = Flask(__name__)

# Beispiel-Datenstruktur für Blogeinträge als Liste von Wörterbüchern
blog_entries = [
    {
        "title": "Erster Blogeintrag",
        "content": "Dies ist der Inhalt meines ersten Blogeintrags."
    },
    {
        "title": "Zweiter Blogeintrag",
        "content": "Dies ist der Inhalt meines zweiten Blogeintrags."
    },
    {
        "title": "Dritter Blogeintrag",
        "content": "Dies ist der Inhalt meines dritten Blogeintrags."
    }
]

# Definiert die Route für die Startseite
@app.route('/')
def index():
    # Rendert die Vorlage 'index.html' und übergibt die Blogeinträge
    return render_template('index.html', entries=blog_entries)

# Definiert die Route für die "Über mich"-Seite
@app.route('/about')
def about():
    # Rendert die Vorlage 'about.html'
    return render_template('about.html')

# Definiert die Route für die "Kontakt"-Seite
@app.route('/contact')
def contact():
    # Rendert die Vorlage 'contact.html'
    return render_template('contact.html')

# Definiert die Route für das Erstellen neuer Blogeinträge
@app.route('/new', methods=['GET', 'POST'])
def new_entry():
    # Überprüft, ob die Methode POST ist (Formular wurde gesendet)
    if request.method == 'POST':
        # Extrahiert den Titel und Inhalt aus dem Formular
        title = request.form['title']
        content = request.form['content']
        # Fügt den neuen Blogeintrag zur Liste hinzu
        blog_entries.append({"title": title, "content": content})
        # Leitet zur Startseite um, nachdem der Eintrag hinzugefügt wurde
        return redirect(url_for('index'))
    # Wenn die Methode GET ist, rendert das Formular für neue Einträge
    return render_template('new_entry.html')

# Startet die Flask-Anwendung im Debug-Modus
if __name__ == '__main__':
    app.run(debug=True)
