
create database victimas_violencia;
use victimas_violencia;

CREATE TABLE tabla_violencia (
    fecha DATE,
    provincia VARCHAR(255),
    genero VARCHAR(20),
    edad INT,
    pais VARCHAR(255),
    violencia_fisica VARCHAR(10),
    violencia_psicologica VARCHAR(10),
    violencia_sexual VARCHAR(10),
    violencia_economica VARCHAR(10),
    violencia_simbolica VARCHAR(10),
    violencia_domestica VARCHAR(10),
    violencia_institucional VARCHAR(10),
    violencia_laboral VARCHAR(10),
    violencia_libertad_reproductiva VARCHAR(10),
    violencia_obstetrica VARCHAR(10),
    violencia_mediatica VARCHAR(10),
    violencia_otras VARCHAR(10),
    vinculo_agresor VARCHAR(255),
    genero_agresor VARCHAR(15)
)

select * from tabla_violencia;

select count(*) from tabla_violencia;
