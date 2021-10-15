// export type Animal = {
//     id: number;
//     peso: number;
//     data_nascimento: string;
//     nome: string;
//     tipo: string;
// };

// export type Page = {
//     page_number: number;
//     page_size: number;
// };

class Animal  {
    id: number = 0;
    peso: number = 0;
    data_nascimento: string = '';
    nome: string = '';
    tipo: string = '';
};

class AnimalPage {
    content?: Animal[];
    page_number: number = 0;
    page_size: number = 0;
};

export {Animal, AnimalPage}