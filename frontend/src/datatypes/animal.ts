//class Animal  {
    //id: number = 0;
    //peso: number = 0;
    //data_nascimento: string = '';
    //nome: string = '';
    //tipo: string = '';
//};

class Animal {
  constructor({id = 0, peso = 0.0, data_nascimento= '', nome = '', tipo = ''} = {}){
    this.id = id;
    this.peso = peso;
    this.data_nascimento = data_nascimento;
    this.nome = nome;
    this.tipo = tipo;
  }
}
class AnimalPage {
    content?: Animal[];
    page_number: number = 0;
    page_size: number = 0;
};

export {Animal, AnimalPage}
