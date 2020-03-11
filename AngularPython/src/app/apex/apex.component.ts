import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Aluno } from './aluno/aluno';

@Component({
  selector: 'app-apex',
  templateUrl: './apex.component.html',
  styleUrls: ['./apex.component.css']
})
export class ApexComponent implements OnInit {

  constructor(private http:HttpClient) { }

  ngOnInit() {
    this.carregaAlunos();
    this.aluno = new Aluno();
  }
  private lista:any = [];
  private aluno:Aluno;
  private texto:string = 'Salvar'
  async carregaAlunos(): Promise<void>{
    await this.http.get('http://localhost:5000').subscribe(result =>{
      this.lista = result;
      console.log(result)
    }, error => console.log(error))
  }
  async salvar():Promise<void>{
    await this.http.post('http://localhost:5000',this.aluno).subscribe(result =>{
      alert(result)
      this.carregaAlunos();
    }, error => console.log(error))
  } 
}
