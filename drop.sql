drop table paciente_citas;
drop table paciente_historia;
drop table pacientetriaje;
drop table paciente_paciente;
drop table medico_medico_experiencias;
drop table medico_medico_eventos;
drop table medico_medico_logros;
drop table medico_medico_publicaciones;
drop table medico_medico_habilidades;
drop table medico_medico_especialidad;
drop table medico_medico_estudios;
drop table medico_medico;
drop table medico_institucion;
drop table medico_especialidad cascade;
drop table django_migrations;

drop table django_content_type cascade;
drop table auth_permission cascade;
drop table auth_group cascade;
drop table auth_group_permissions;
drop table auth_user_groups;
drop table auth_user_user_permissions;
drop table django_admin_log ;
drop table django_session;

drop table administrador_inbox;
drop table administrador_usuario;
drop table auth_user cascade;
drop table auth_user_groups;
drop table auth_user_user_permissions;
drop table django_admin_log;
drop table medico_medico_citas cascade;
drop table medico_medico_diagnostico cascade;
drop table medico_medico_informe cascade;
drop table medico_medico_revision cascade;
drop table medico_referencia cascade;
drop table medico_emergencia cascade;
drop table medico_institucion cascade;
drop table medico_medico cascade;

drop table paciente_historiadetriaje;
drop table paciente_paciente;
drop table administrador_usuario;


-- alter table django_content_type ADD column name varchar(30);
-- create table administrador_usuario(id varchar(30) primary key, user_id varchar(30), ci varchar(30) unique);