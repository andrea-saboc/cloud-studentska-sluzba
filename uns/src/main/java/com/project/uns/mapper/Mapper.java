package com.project.uns.mapper;

import org.springframework.stereotype.Component;

import com.project.uns.dto.RegisterDto;
import com.project.uns.model.Professor;
import com.project.uns.model.Student;

@Component
public class Mapper {

    public Student mapStudent(RegisterDto dto) {
        Student student = new Student();
        student.setJmbg(dto.getJmbg());
        student.setSurame(dto.getSurname());
        student.setName(dto.getName());

        return student;
    }
    
    public Professor mapProfessor(RegisterDto dto) {
        Professor professor = new Professor();
        professor.setJmbg(dto.getJmbg());
        professor.setSurname(dto.getSurname());
        professor.setName(dto.getName());
        
        return professor;
    }
    
}
