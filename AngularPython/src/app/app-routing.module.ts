import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ApexComponent } from './apex/apex.component';


const routes: Routes = [
  {path:'',component:ApexComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
