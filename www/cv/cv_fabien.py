from datetime import datetime

def index(error=''):
    delta = datetime.now() - datetime(1992,12,7)
    age = delta.days//365

    html = '''<!DOCTYPE html>

<html>

    <head>
        <meta charset="utf-8"/>
        <title>CV - BONNEVAL Fabien</title>
        <link rel="stylesheet" href="../cv.css" />
    </head>

    <body>
    <header>
        <div id="retour"><br/><a href="../../page_cv.py/index" title="asasourdoire" >Retour au site</a></div>
        <div id="title">
            <h1>BONNEVAL Fabien<br/><br/>Etudiant à l'ENAC<br/>Première année du cycle ingénieur</h1><br/>

    </div>
        <div id="photo">
            <img width="100px" src="../fabien.png" alt="Fabien">
        </div>
            <p>Louradour<br/>
            19120 La Chapelle Aux Saints<br/>
            <span class="mail" >fabien.bonneval@gmail.com</span></br>
            Permis B</br>
            Nationalité française</br>
            {0} ans
            </p>
    </header>

    <section>
    <h1>Formation</h1>
    <ul>
            <li><strong>2013-2015 :</strong> Première année d'école d'ingénieur à l'ENAC à Toulouse.</li>
        </ul>
        <ul>
            <li><strong>2011-2013 :</strong> Première et deuxième année en CPGE, lycée scientifique et technologique Georges Cabanis, option Technologie et Sciences de l'Ingénieurs.</li>
        </ul>


        <h1>Diplômes</h1>
        <ul>
            <li><strong>juin 2010 :</strong> Baccalauréat technologique (STI génie Mécanique).</li>
        </ul>

        <h1>Expériences</h1>

        <ul>
            <li><strong>2014 (1 mois) : </strong> Stage à l'entreprise FGD, Saint Céré</li>
        </ul>
        <ul>
            <li><strong>2008-2013 : </strong> Travaux agricoles saisonniers : travail de la vigne, récolte du tabac</li>
        </ul>



        <h1>Compétences</h1>

        <ul>
        <li><strong>Langues :</strong>  anglais (intermédiaire)</li>
        <li><strong>Software :</strong> Usage régulier de linux (Ubuntu) et Windows, CAO: SolidWorks</li>
        <li><strong>Programmation :</strong> Langage C, Python</li>
        </ul>



        <h1>Loisirs et Associations</h1>
        <ul>
            <li><strong>Technique :</strong>Club robotique: conception et construction d'un robot pour participer à la coupe de France de robotique: conception et programmation de systèmes embarqués.</li>
            <li><strong>Musique, Associatif :</strong>Trompette, membre d’une société de musique, Fanfare, club Jazz.</li>
        </ul>
    </section>
    </body>

    </html>
    '''.format(age)
    return html
