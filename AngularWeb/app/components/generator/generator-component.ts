import { Component, OnInit, NgModule } from '@angular/core';
import { GeneratorService } from './generator-service'
import { IGeneratorText } from './generator-text-interface'
import { IGeneratorGenerate } from './generator-generate-interface';

@Component({
  selector: 'generator',
  templateUrl: 'views/generator.html',
  providers: [GeneratorService]
})

export class GeneratorComponent implements OnInit{
  constructor(private _generatorService: GeneratorService) { }

  text: IGeneratorText;
  generated: IGeneratorGenerate;

  ngOnInit() {
    this._generatorService.getText().subscribe(text => this.text = text);
  }

  generate(numOfHeroes: number) {
    this._generatorService.generate(numOfHeroes).subscribe(g=> this.generated = g);
  }
}
