<template>
    <section class="section" style="margin-top: 3%;">
            <div class="container">
                    <div class="row">
                        <div class="col-md-12">


                            <b-form-input v-model="search" name="search" placeholder="Search Book by Name"></b-form-input>
                            <b-button v-b-modal.modal-1>Add Book</b-button>

                             <!-- <treeselect v-model="value" :multiple="true" :options="options" />  -->
                             <!-- <treeselect v-model="value"  :options="options"/>  -->
                                          
                            <br>

                            <b-table 
                            striped hover 
                            :items="filteredItems" 
                            :fields="fields" 
                            stacked="md" 
                            show-empty
              
                            small>
                    
                                <template v-slot:cell(actions)="{ item }">
                                     <span><b-btn v-b-modal.modal-2 @click="editBook(item.id)">Edit</b-btn></span>
                                     <span><b-button @click="deleteBook(item.id)">Delete</b-button></span>
                                </template>

                            </b-table>

                            <b-modal id="modal-1" title="Create New Book">
                                <b-form @submit="saveBook">

                                        <b-form-group
                                                id="input-group-1"
                                                label="Book Name:"
                                                label-for="input-1">

                                                <b-form-input
                                                    id="input-1"
                                                    v-model="name"
                                                    type="text"
                                                    required>
                                                </b-form-input>
                                      </b-form-group>
                                      <b-form-group
                                            id="input-group-1"
                                            label="Author Name:"
                                            label-for="input-1">

                                            <!-- <b-form-input
                                                id="input-1"
                                                v-model="author_name"
                                                type="text"
                                                required>
                                            </b-form-input> -->

                                          <treeselect v-model="author_name"  :options="options"/>    
                                       </b-form-group>

                                      

                                        <b-form-group
                                                id="input-group-1"
                                                label="Number of Pages:"
                                                label-for="input-1">

                                                <b-form-input
                                                    id="input-1"
                                                    v-model="number_of_pages"
                                                    type="text"
                                                    required>
                                                </b-form-input>
                                        </b-form-group>


                                   <b-button type="submit" variant="primary">Submit</b-button>
                                </b-form>    
                             </b-modal>



                              <b-modal id="modal-2" title="Edit Book">
                                    <b-form @submit="updateBook">

                                            <b-form-group
                                                    id="input-group-1"
                                                    label="Book Name:"
                                                    label-for="input-1">

                                                    <b-form-input
                                                        id="input-1"
                                                        v-model="name"
                                                        type="text"
                                                        required>
                                                    </b-form-input>
                                          </b-form-group>
                                          <b-form-group
                                                id="input-group-1"
                                                label="Author Name:"
                                                label-for="input-1">

                                                <!-- <b-form-input
                                                    id="input-1"
                                                    v-model="author_name"
                                                    type="text"
                                                    required>
                                                </b-form-input> -->
                                             <treeselect v-model="author_name"  :options="options"/>       
                                           </b-form-group>

                                            <b-form-group
                                                    id="input-group-1"
                                                    label="Number of Pages:"
                                                    label-for="input-1">

                                                    <b-form-input
                                                        id="input-1"
                                                        v-model="number_of_pages"
                                                        type="text"
                                                        required>
                                                    </b-form-input>
                                            </b-form-group>


                                       <b-button type="submit" variant="primary">Submit</b-button>
                                    </b-form>    
                                 </b-modal>



                        </div>
                    </div>
            </div>
     </section>
</template>


<script>

import Treeselect from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'

import BookService from "../services/BookService";
import AuthorService from "../services/AuthorService";
import auth from '~/middleware/auth';

export default {
    components: { Treeselect },
    data() {
        return {
            //options: [{id: 'a',label: 'a',children: [{id: 'aa',label: 'aa',}, {id: 'ab',label: 'ab', }], }, {id: 'b',label: 'b',}, {id: 'c', label: 'c',}],
            options: [{id: 'a',label: 'a' }, { id: 'b', label: 'b', }, { id: 'c', label: 'c', }],
            search: '',
            id: null,
            name: null,
            author_name: null,
            number_of_pages: null,
            error: null,
            fields: [{ key: 'id', sortable: true }, { key: 'name'}, { key: 'author_name' }, { key: "number_of_pages" }, { key: "actions" }],
            books: [{ id: "1", name: "Purple Hibiscus", number_of_books:"3" }, { id: "2", name: "Arrow of God", number_of_books: "1"  }]
        }
    },

    async created() {
        this.getBooks();
        this.getAuthors();
    },
    computed: {
        filteredItems() {
            if (this.search.trim() === '') {
                return this.books;
            }
            const searchTerm = this.search.toLowerCase();
            return this.books.filter(item => item.name.toLowerCase().includes(searchTerm));
        }
    },
    watch: {
        search(newvalue, oldvalue) {
            console.log('Search Text Changed:', newvalue);
        }
    },

    methods: {
        getAuthors() {
            AuthorService.fetchAuthor().then((response) => {
                var author = [];
                response.data.forEach(element => {
                    author.push({ id: element.id, label: element.name });
                });
                 this.options = author;
                 console.log(author);
                //this.$toast.success(response, { icon: "done" });
            }).catch((response) => {
                console.log(response);
                this.$toast.success(response, { icon: "Failed" });
            });
        },
        getBooks() {
             BookService.fetchBook().then((response) => {
                console.log(response.data);
                this.books = response.data;
                //this.$toast.success(response, { icon: "done" });
            }).catch((response) => {
                console.log(response);
                this.$toast.success(response, { icon: "Failed" });
            });
        },
        saveBook() {
            event.preventDefault();
            //this.resetBook();
            console.log("Saving Book ..");
            
            var data = { "name": this.name, "author_name": this.author_name, "number_of_pages": this.number_of_pages, "author_id": this.author_name };
            BookService.saveBook(data).then((response) => {
                console.log(response.data);
                this.resetBook();
                this.getBooks();
                this.$toast.success("Added new book succesfully", { icon: "done" });
            }).catch((response) => {
                console.log(response.data);
                this.$toast.success(response.data, { icon: "Failed" });
            });
        },
        editBook(value) {
            event.preventDefault();
            const result = this.books.find((item) => item.id == value);
            this.id = result.id;
            this.name = result.name;
            this.author_name = result.author_name;
            this.number_of_pages = result.number_of_pages;
        },
        updateBook() {
            event.preventDefault()
            console.log("updating ..");

            var result = this.options.find((element) => element.label == this.author_name);

            //console.log(result.id);

            var data = {"id": this.id, "name": this.name, "author_name": this.author_name,
                 "number_of_pages": this.number_of_pages, "author_id": result.id};
            BookService.updateBook(data, data.id).then((response) => {
                console.log(response.data);
                this.resetBook();
                this.getBooks();
                this.$toast.success("Updated Book succesfully", { icon: "done" });
            }).catch((response) => {
                console.log(response.data);
                this.$toast.success(response.data, { icon: "Failed" });
            });
        },
        deleteBook(value) {
             event.preventDefault();
             console.log(value);
             
             BookService.deleteBook(value).then((response) => {
                console.log(response.data);
                this.resetBook();
                this.getBooks();
                this.$toast.success("Deleted Book succesfully", { icon: "done" });
            }).catch((response) => {
                console.log(response.data);
                this.$toast.success(response.data, { icon: "Failed" });
            });
            
        },
        resetBook() {
            this.name = null;
            this.author_name = null;
            this.number_of_pages = null;
        },

    },
}

</script>