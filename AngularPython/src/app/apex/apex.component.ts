import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-apex',
  templateUrl: './apex.component.html',
  styleUrls: ['./apex.component.css']
})
export class ApexComponent implements OnInit {

  constructor(private http:HttpClient) { }

  ngOnInit() {
    this.carregaAlunos();
  }
  private lista:any = [];
  async carregaAlunos(): Promise<void>{
    await this.http.get('http://localhost:5000').subscribe(result =>{
      this.lista = result;
      console.log(result)
    }, error => console.log(error))
  }
}
