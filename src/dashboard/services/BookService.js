import axios from 'axios';
import {state} from '~/store/index';

const BASE_URL = process.env.BASEURL + "books/"
const headers =  {
        'Authorization':'Bearer '+ state().token,
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8'
};
class BookService{

    saveBook(author){
        return axios.post(BASE_URL,author,{headers:headers});
    }
    fetchBook(){
        console.log(process.env.BASEURL);
        return axios.get(BASE_URL,{headers:headers});
    }
    updateBook(author,id){
         return axios.put(BASE_URL+id,author,{headers:headers});
    }
    deleteBook(id){
         return axios.delete(BASE_URL+id,{headers:headers});
    }

}
export default new BookService();

