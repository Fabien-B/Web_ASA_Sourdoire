def index(error=''):
    html = '''<!DOCTYPE html>

<html>

    <head>
        <meta charset="utf-8"/>
        <title>CV - BUISAN Guilhem</title>
        <link rel="stylesheet" href="../cv.css" />
    </head>

    <body>
    <header>
        <div id="retour"><br/><a href="../../page_cv.py/index" title="asasourdoire" >Retour au site</a></div>
        <div id="title">
            <h1>BUISAN Guilhem<br/><br/>Etudiant à l'ENAC<br/>Première année du cycle ingénieur</h1><br/>

     </div>
        <div id="photo">
            <img width="100px" src="../Buisan.png" alt="Guilhem">
        </div>
            <p>9, carrer de Cal Joanet<br/>
            66800 ERR<br/>
            Tel : <strong>06 87 79 88 17</strong><br />
            <span class="mail" >buisanguilhem@gmail.com</span>
            </p>
    </header>

    <section>
    <h1>Formation</h1>
    <ul>
            <li><strong>2014-2015 :</strong> Première année à l'ENAC, Toulouse cycle ingénieur</li>
        </ul>
        <ul>
            <li><strong>2012-2014 :</strong> CPGE, lycée Arago, Perpignan</li>
        </ul>


        <h1>Diplômes</h1>
        <ul>
            <li><strong>Juillet 2012 :</strong> Brevet de Base de Pilote d'Avion</li>
            <li><strong>Juin 2012 : </strong>Baccalauréat Série S-SVT Mention Très Bien, Font-Romeu, Académie de Montpellier</li>
        </ul>

        <h1>Expériences Professionnelles</h1>

        <ul>
            <li><strong>Juillet 2011 : </strong>Osséja - France, LA SOLANE, Secteur : Services généraux Poste occupé : Employé de services généraux</li>
        </ul>
        <ul>
            <li><strong>Juillet 2009 :</strong> Riscle - France, EARL d'ARGENTON, Secteur : Agricole; Poste occupé : Contrat saisonnier pour les travaux de castration du maïs</li>
        </ul>


        <h1>Compétences</h1>

        <ul>
        <li>Décrire, décomposer, résoudre, critiquer et discuter des problèmes physiques  et mathématiques complexes.</li>
        <li>Parler, écrire et traduire l'anglais.</li>
        <li>Appliquer les consignes d'hygiène et de sécurité relatives à l'entretien des locaux en milieu hospitalier.</li>
        </ul>



        <h1>Loisirs et Associations</h1>
        <ul>
            <li>Membre du club Robotique de l'ENAC</li>
            <li>Maîtrise de Windows XP/Vista/7/8, Linux Mint/Ubuntu</li>
            <li>Maîtrise du C, C++, Python, Javascript, HTML, SQL</li>
            <li>Notions de réseau</li>
        </ul>
    </section>
    </body>

    </html>
    '''
    return html
