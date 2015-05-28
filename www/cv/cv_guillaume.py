def index(error=''):
    html = '''<!DOCTYPE html>

<html>

    <head>
        <meta charset="utf-8"/>
        <title>CV - PASTRE Guillaume</title>
        <link rel="stylesheet" href="../cv.css" />
    </head>

    <body>
    <header>
        <div id="retour"><br/><a href="../../page_cv.py/index" title="asasourdoire" >Retour au site</a></div>
        <div id="title">
            <h1>PASTRE Guillaume<br/><br/>Etudiant à l'ENAC<br/>Première année du cycle ingénieur</h1><br/>

     </div>
        <div id="photo">
            <img width="100px" src="../Pastre.jpg" alt="Guillaume">
        </div>
            <p>Chambre 339 Résidence Védrines, 7 Avenue Edouard Belin<br/>
            31055 TOULOUSE<br/>
            Tel : <strong>06 58 40 54 88</strong><br />
            <span class="mail" >guillaume.pastre@alumni.enac.fr</span>
            </p>
    </header>

    <section>
    <h1>Formation</h1>
    <ul>
            <li><strong>2014-2015 :</strong> Première année d'école d'ingénieur à l'ENAC à Toulouse.</li>
        </ul>
        <ul>
            <li><strong>2012-2014 :</strong>Classe préparatoire aux grandes écoles, lycée Joffre, Montpellier filière MP</li>
        </ul>


        <h1>Diplômes</h1>
        <ul>
            <li><strong> 2012 :</strong> Baccalauréat scientifique mention Bien, option « Sciences de la Vie et de la Terre » au lycée Emmanuel d'Alzon à Nîmes </li>
            <li><strong> 2011 :</strong> Brevet d'inititation à l'aéronautique </li>
        </ul>

        <h1>Expériences Professionnelles</h1>

        <ul>
            <li><strong>2009 : </strong> Découverte de l'entreprise Adrea Mutuelle à l'agence de Nîmes.</li>
        </ul>



        <h1>Compétences</h1>

        <ul>
        <li><strong>Langues :</strong>  anglais courant</li>
        <li><strong>Software :</strong> Usage des suites bureautiques Windows et Ubuntu</li>
        <li><strong>Programmation :</strong> Python</li>
        <li><strong>Divers :</strong> Permis B</li>
        </ul>



        <h1>Loisirs et Associations</h1>
        <ul>
            <li>Voyages à l'étranger : Irlande, Ecosse, Angleterre, Etats-Unis</li>
        </ul>
    </section>
    </body>

    </html>
    '''
    return html
