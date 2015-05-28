import mysql.connector

class Message(object):
    database = 'IENAC14_asa'
    user = 'root'
    password = 'root'
    host = '127.0.0.1'

    def __init__(self,id_mess,date=None,objet=None,corps=None,nom=None,numero=None, id_exploitant=None):
        if  id_mess>0:
            self.load(id_mess)
        else:
            connection = mysql.connector.connect(user=Message.user, password=Message.password,host=Message.host,database=Message.database)
            curseur = connection.cursor()
            requete = 'select max(Id_message) from Message;'
            curseur.execute(requete)
            (maxId,)=curseur.fetchall()[0]
            if maxId is None: maxId = 0
            self.id = maxId + 1
            self.date = date
            self.nom = nom
            self.numero = numero
            self.objet = objet
            self.corps = corps
            self.id_exploitant = id_exploitant
            curseur.close()
            connection.close()

    def save(self):
        connection = mysql.connector.connect(user=Message.user, password=Message.password,host=Message.host,database=Message.database)
        curseur = connection.cursor()
        requete = """
        INSERT INTO Message VALUES ({0},"{1}","{2}","{3}","{4}","{5}","{6}");""".format(self.id, self.date, self.objet, self.corps, self.nom, self.numero, self.id_exploitant)
        curseur.execute(requete)
        connection.commit()
        curseur.close()
        connection.close()

    def load(self,id_mess):
        connection = mysql.connector.connect(user=Message.user, password=Message.password,host=Message.host,database=Message.database)
        curseur = connection.cursor()
        requete = 'select * from Message where Id_message={};'.format(id_mess)
        curseur.execute(requete)
        try:
            (_,date,objet,corps,nom,numero,id_exploitant)=curseur.fetchall()[0]
        except IndexError:
            raise MessageError("Message with id {} doesn't exist".format(id_mess))
        curseur.close()
        connection.close()

        self.id = id_mess
        self.date = date
        self.nom = nom
        self.numero = numero
        self.objet = objet
        self.corps = corps
        self.id_exploitant = id_exploitant

    @staticmethod
    def get_all_messages():
        connection = mysql.connector.connect(user=Message.user, password=Message.password,host=Message.host,database=Message.database)
        curseur = connection.cursor()
        requete = 'SELECT Id_message from Message;'
        curseur.execute(requete)
        Id_message_list = curseur.fetchall()
        message_list = []
        for i in range(1, len(Id_message_list)):
            message_list.append(Message(Id_message_list[i][0]))
        curseur.close()
        connection.close()
        return message_list

    @staticmethod
    def delete_all():
        connection = mysql.connector.connect(user=Message.user, password=Message.password,host=Message.host,database=Message.database)
        curseur = connection.cursor()
        requete = 'DELETE from Message;'
        curseur.execute(requete)
        message_list = []
        connection.commit()
        curseur.close()
        connection.close()

class MessageError(Exception):
    pass
