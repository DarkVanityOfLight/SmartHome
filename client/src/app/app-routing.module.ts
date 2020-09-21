import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { StartComponent } from 'src/bundles/sites/start/start.component';
import { GarageComponent } from 'src/bundles/sites/garage/garage.component';

const routes: Routes = [
  { path: '', component: StartComponent },
  { path: 'Garage', component: GarageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
