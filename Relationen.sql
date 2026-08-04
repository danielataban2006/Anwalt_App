create table Mandant(
    M_ID int auto_increment primary key,
    Vorname varchar not null,
    Nachname varchar not null,
    Adresse varchar not null,
    Telefon varchar,
    EMail varchar 
)

create table Gegner_Partei(
    GP_ID int auto_increment primary key,
    Name varchar,
    Typ varchar,
    Telefon varchar,
    EMail varchar,
    Adresse varchar
)

create table Fall_wird_geöffnet_von(
    M_ID int,
    GP_ID int,
    Fall_ID int,
    primary key(M_ID, GP_ID, Fall_ID),
    foreign key(M_ID) references Mandant(M_ID),
    foreign key(GP_ID) references Gegner_Partei(GP_ID),
    foreign key(Fall_ID) references Fall(Fall_ID)
)


create table Fall(
    Fall_ID int auto_increment primary key,
    Datum_des_Einreichens date,
    Datum_des_Lösens date,
    Bearbeitungsstatus varchar not null check(Bearbeitungsstatus in('neu',
    'in Bearbeitung','wartet auf Mandant','wartet auf Gegner','erledigt','archiviert')),
    Beschreibung varchar,
    Z_ID int not null,
    foreign key(Z_ID) references Zeiterfassung(Z_ID),
)

create table Dokument(
    D_ID int auto_increment primary key,
    Titel varchar,
    Kategorie varchar,   #hier könnte man eine vorgegebene Menge machen
    Dateipfad varchar,
    Gültigkeit date
) 

create table Aufgabe(
    A_ID integer auto_increment primary key,
    Bezeichnung varchar,
    benötigte_Zeit uint default 0 check(benötigte_Zeit)
    Ort varchar,
    Datum date,
    Uhrzeit time,
    hat_Frist boolean default false,

    Z_ID int not null,
    foreign key(Z_ID) references Zeiterfassung(Z_ID),

    Fall_ID int not null,
    foreign key (Fall_ID) references Fall(Fall_ID),    
    A_status varchar not null check(A_status in('erledigt','verschoben','offen')),
    Benötigte_Zeit uinteger default 0
)

create table Zeiterfassung(
    Z_ID int auto_increment primary key,
    zu_zahlende_Summe int default 0 check(zu_zahlende_Summe>=0),
    Status_Bezahlung varchar default 'noch offen' check(Status in('noch offen', 'gezahlt')),
    Beschreibung varchar,
    Zeit_Gesammt time default 0,
    Fall_ID int not null,
    foreign key (Fall_ID) references Fall(Fall_ID),
)

create table Fall_benötigt_Dokument(
    D_ID int,
    F_ID int,
    primary key(D_ID, F_ID),
    foreign key(D_ID) references Dokument(D_ID),
    foreign key(F_ID) references Fall(F_ID)
)

create table Aufgabe_benötigt_Dokument(
    A_ID int,
    D_ID int,
    primary key(A_ID, D_ID),
    foreign key(A_ID) references Aufgabe(A_ID),
    foreign key(D_ID) references Dokument(D_ID)
)