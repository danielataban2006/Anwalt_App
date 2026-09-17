import sqlite3
import relations

con=sqlite3.connect("Anwalt_APP.db")  # Verbinde dich mit der Datenbank (con ist also die Variable in der die Verbindung zur Datenbank gespeichert wird)

cursor=con.cursor() # cursor ist der Zeiger der Datenbank

def insertintodb():
    gewuenschte_Relation=input("Was ist neu? [ neuer Fall (1) neue Aufgabe (2) neues Dokument (3) ] ")
    if gewuenschte_Relation=="1":    # neuen Fall einfügen zusammen mit den Informationen die zwingend dazugehören
        try:

            new_mandant=input("haben wir einen neuen Mandanten? (ja/nein) ")
            mandanten_liste=[]
            while(new_mandant=="ja"):
                cursor.execute(""" SELECT MAX(M_ID) FROM Mandant """)
                max_m_ID=cursor.fetchone()
                if max_m_ID is None:
                    m_ID=0
                else:
                    m_ID=max_m_ID[0]+1
                mandanten_liste.append(m_ID)
                print("neuer Mandant")
                vorname=input("Vorname: ")
                nachname=input("Nachname: ")
                adresse=input("Adresse: ")
                telefon=input("Telefon: ")
                email=input("E_Mail: ")
                Mandant_werte=(m_ID, vorname, nachname, adresse, telefon, email)
                sql = "INSERT INTO Mandant VALUES(?, ?, ?, ?, ?)"
                cursor.execute(sql, Mandant_werte)
                new_mandant=input("haben wir einen neuen Mandanten? (ja/nein) ")

            old_mandant=input("gehören noch uns bekannte Mandanten zum Fall? (ja/nein) ")
            while (old_mandant=="ja"):
                vorname=input("Vorname ")
                nachname=input("Nachname ")
                cursor.execute(""" SELECT M_ID FROM Mandant WHERE Vorname=? AND Nachname=?""")
                m_ID=cursor.fetchone()[0]
                mandanten_liste.append(m_ID)
                old_mandant=input("gehören noch uns bekannte Mandanten zum Fall? (ja/nein) ")
            
            new_gegner=input("Haben wir einen neuen Gegner? (ja/nein) ")
            gegner_liste=[]
            while(new_gegner=="ja"):
                cursor.execute(""" SELECT MAX(M_ID) FROM Gegner_Partei""")
                max_g_ID=cursor.fetchone()
                if max_g_ID is None: 
                    g_ID=0
                else:
                    g_ID=max_g_ID[0]+1
                gegner_liste.append(z_ID)
                print("neue Gegner-Partei ")
                name=input("Name: ")
                typ=input("Typ: ") 
                telefon=input("Telefon: ")
                email=input("E_Mail: ")
                adresse=input("Adresse: ") 
                Gegnerpartei_werte=(g_ID, name, typ, telefon, email, adresse)
                sql="INSERT INTO Gegner-Partei VALUES(?,?,?,?,?,?)"
                cursor.execute(sql, Gegnerpartei_werte)
                new_gegner=input("Haben wir einen neuen Gegner? ")

            old_gegner=input("gehören noch uns bekannte Gegner zum Fall? (ja/nein) ")
            while (old_gegner=="ja"):
                vorname=input("Name ")
                nachname=input("Typ ")
                cursor.execute(""" SELECT G_ID FROM Gegner_Partei WHERE Name=? AND Typ=? """)
                m_ID=cursor.fetchone()[0]
                gegner_liste.append(g_ID)
                old_gegner=input("gehören noch uns bekannte Gegner zum Fall? ")

            print("Zeiterfassung")
            cursor.execute(""" SELECT MAX(Z_ID) FROM Zeiterfassung""")
            max_z_ID=cursor.fetchone()
            if max_z_ID is None: # falls die tabelle zeiterfassung nicht leer ist
                z_ID=0
            else:
                z_ID=max_z_ID[0]+1
            beschreibung=input("Beschreibung")
            zeiterfassung_werte=(z_ID, beschreibung)
            sql="INSERT INTO Zeiterfassung (Z_ID, Beschreibung) VALUES(?,?)"
            cursor.execute(sql, zeiterfassung_werte)

            print("neuer Fall ")
            cursor.execute(""" SELECT MAX(F_ID) FROM Fall """)
            max_f_ID=cursor.fetchone()
            if max_f_ID is None: # ist die tabelle Fall nicht leer?
                f_id=0 #ermittle den Fall mit der größten id und speichere diese id
            else:
                f_id=max_f_ID[0]+1 
            dateein=input("Datum des Einreichens: ")
            Beschreibung=input("Beschreibung: ")
            Fall_werte=(f_id, dateein,Beschreibung,z_ID)
            sql="INSERT INTO Fall (F_ID, Datum_des_Einreichens, Beschreibung, Z_ID) VALUES(?,?,?,?)"
            cursor.execute(sql,Fall_werte)
            
            for x in mandanten_liste:
                for y in gegner_liste:
                    Geoeffnet_von_werte=(x,y,f_id)
                    sql="INSERT INTO Fall_wird_geöffnet_von VALUES(?,?,?)"
                    cursor.execute(sql,Geoeffnet_von_werte)

            con.commit()

        except: 
            print("Ein Problem ist aufgetreten --> automatischer Rollback")
            con.rollback()
            raise

