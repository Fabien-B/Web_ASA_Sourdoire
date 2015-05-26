def index(error=''):
    html = '''<!DOCTYPE html>

<html>

    <head>
        <meta charset="utf-8"/>
        <title>CV - DZIECIOL Niolas</title>
        <link rel="stylesheet" href="../cv.css" />
    </head>

    <body>
    <header>
        <div id="retour"><br/><a href="../../index.py/index" title="asasourdoire" >Retour au site</a></div>
        <div id="title">
            <h1>DZIECIOL Nicolas<br/><br/>Etudiant à l'ENAC<br/>Première année du cycle ingénieur</h1><br/>

     </div>
        <div id="photo">
            <img width="100px" src="../polo.png" alt="Nicolas">
        </div>
            <p>101 rue Saint Roch<br/>
            31400 TOULOUSE<br/>
            <span class="mail" >nicolas.dzieciol@gmail.com</span>
            </p>
    </header>

    <section>
    <h1>Formation</h1>
    <ul>
            <li><strong>2013-2015 :</strong> Première année d'école d'ingénieur à l'ENAC à Toulouse.</li>
        </ul>
        <ul>
            <li><strong>2011-2013 :</strong> Première et deuxième année en CPGE, lycée scientifique et technologique Gustave Eiffel (Dijon), option Technologie et Sciences de l'Ingénieurs.</li>
        </ul>


        <h1>Diplômes</h1>
        <ul>
            <li><strong>juin 2011 :</strong> Baccalauréat technologique (STI génie Électrotechnique).</li>
        </ul>

        <h1>Expériences Professionnelles</h1>

        <ul>
            <li><strong>2013 (2 mois) : </strong> SEGER : Emploi saisonnier, monteur électricien à Montbard.</li>
        </ul>
        <ul>
            <li><strong>2012 (2 mois) :</strong> SNCF : Emploi saisonnier, ASCT (Agent du service commercial trains) à Dijon.</li>
        </ul>


        <h1>Compétences</h1>

        <ul>
        <li><strong>Langues :</strong>  anglais (intermédiaire)</li>
        <li><strong>Software :</strong> Usage régulier de Windows et Ubuntu. Suite Microsoft Office, Autodesk Inventor, Adobe Photoshop.</li>
        <li><strong>Programmation :</strong> Langage C, Python</li>
        <li><strong>Divers :</strong> Permis B</li>
        </ul>



        <h1>Loisirs et Associations</h1>
        <ul>
            <li><strong>Divers :</strong> Informatique, photographie.</li>
        </ul>
    </section>
    </body>

    </html>
    '''
    return html