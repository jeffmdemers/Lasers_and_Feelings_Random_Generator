import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable'
import 'rxjs/add/operator/map';

import { IGeneratorText } from './generator-text-interface';
import { IGeneratorGenerate } from './generator-generate-interface';

@Injectable()
export class GeneratorService {
  constructor (private _http: Http) {}

  getText() : Observable<IGeneratorText> {
    return this._http.get("http://127.0.0.1:5000/Text")
      .map((res:Response) => <IGeneratorText>res.json());
  }

  generate(numOfHeroes: number) : Observable<IGeneratorGenerate>{
    return this._http.post("http://127.0.0.1:5000/Generate", {"numberOfHeroes": numOfHeroes})
      .map((res:Response) => <IGeneratorGenerate>res.json());
  }
}
