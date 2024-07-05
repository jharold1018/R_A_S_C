create database rasc;
use rasc;
create table P_siga(
cedula int (20) primary key,
nombre varchar(200),
ocupacion varchar(300)
);

create table registro(
numero int auto_increment primary key,
nombre VARCHAR(100) not null,
nombre_cientifico varchar(100) not null,
tipo_de_especie varchar(100) not null,
veneno varchar(2) not null,
habitos varchar(1000) not null,
habitat varchar(100) not null,
fecha_avistamiento char (9),
escamas varchar(2) not null
);

create table avistamiento(
numero int primary key auto_increment,
ubicacion varchar(200),
hora char(7) not null,
aspecto varchar (1000) not null,
ataco varchar(2) not null,
imagen char not null
);

create table avistador(
id int primary key auto_increment,
ficha int(8),
nombre varchar(200),
correo varchar(100)
); 

create table mapa(
cordenada float primary key not null,
nombre varchar(200),
color varchar(300),
veneno varchar(2)
);

alter table registro add cedula_siga_fk int;
alter table registro add foreign key (cedula_siga_fk) references p_siga (cedula);
alter table avistamiento add id_fk int;
alter table avistamiento add foreign key (id_fk) references avistador(id);
