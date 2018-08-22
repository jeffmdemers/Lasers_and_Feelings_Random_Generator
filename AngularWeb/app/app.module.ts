import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import { GeneratorComponent } from './components/generator/generator-component';
import { HttpModule } from '@angular/http';

@NgModule({
  imports:      [ BrowserModule, HttpModule ],
  declarations: [ AppComponent, GeneratorComponent],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
