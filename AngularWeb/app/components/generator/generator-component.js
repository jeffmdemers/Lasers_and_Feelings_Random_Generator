"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require("@angular/core");
var generator_service_1 = require("./generator-service");
var GeneratorComponent = (function () {
    function GeneratorComponent(_generatorService) {
        this._generatorService = _generatorService;
    }
    GeneratorComponent.prototype.ngOnInit = function () {
        var _this = this;
        this._generatorService.getText().subscribe(function (text) { return _this.text = text; });
    };
    GeneratorComponent.prototype.generate = function (numOfHeroes) {
        var _this = this;
        this._generatorService.generate(numOfHeroes).subscribe(function (g) { return _this.generated = g; });
    };
    return GeneratorComponent;
}());
GeneratorComponent = __decorate([
    core_1.Component({
        selector: 'generator',
        templateUrl: 'views/generator.html',
        providers: [generator_service_1.GeneratorService]
    }),
    __metadata("design:paramtypes", [generator_service_1.GeneratorService])
], GeneratorComponent);
exports.GeneratorComponent = GeneratorComponent;
//# sourceMappingURL=generator-component.js.map