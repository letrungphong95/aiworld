<template>
    <div>
        <v-card color="blue lighten-3">
            <v-card-title class="text-center justify-center">
                <h3 class="font-weight-bold display-2 basil--text">Dog or Cat ?</h3>
            </v-card-title>
        </v-card>
        <v-layout row align="center" justify="center">
            <v-flex sm2 offset-sm2>
                <v-flex mt-6 mb-6>
                    <v-btn 
                        raised 
                        class="primary" 
                        width="400"
                        @click="onPickFile">Upload Image
                    </v-btn>    
                    <input 
                        type="file" 
                        style="display:none" 
                        ref="fileInput" 
                        accept="image/*"
                        @change="onFilePicked">
                </v-flex>
                <v-flex v-if="showImage==1 || showImage==2" mt-6 mb-6>
                    <v-btn 
                        raised 
                        width="400"
                        class="primary"
                        color="error"
                        @click="predictFile">Predict
                    </v-btn>
                </v-flex>
                <v-flex v-if="showImage==2" mt-6 mb-6>
                    <v-alert type="success">
                        <h3> This is a {{ label }}</h3>
                        <h3> Score: {{ scores }}</h3>
                    </v-alert>
                </v-flex>
            </v-flex>
        <v-flex sm6 offset-sm2 mt-2 mb-2>
            <v-img
                v-if="showImage"
                :src="imageUrl"
                aspect-ratio="1"
                class="grey lighten-2"
                max-width="500"
                max-height="300"
            ></v-img>
        </v-flex>
        </v-layout>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data(){
            return {
                imageUrl: "",
                showImage: 0,
                image: null,
                label: "",
                scores: ""
            }
        },
        computed: {
            formIsValid() {
                return this.imageUrl !== ''
            }
        },
        methods: {
            onPickFile () {
                this.$refs.fileInput.click();
            },
            onFilePicked (event) {
                const files = event.target.files;
                let filename = files[0].name;
                if (filename.lastIndexOf('.') <= 0){
                    return alert("Please add a valid file!");
                }''
                const fileReader = new FileReader();
                fileReader.addEventListener('load', () => {
                    this.imageUrl = fileReader.result;
                    this.showImage = 1;
                });
                fileReader.readAsDataURL(files[0]);
                
            },
            predictFile() {
                const fd = new FormData();
                fd.append('image_path',this.image);
                axios.post('http://127.0.0.1:8000/api/object-label', {
                    "image_path": this.imageUrl
                })
                .then(res => {
                    this.label = res.data.label;
                    this.scores = res.data.scores;
                    this.showImage = 2;
                })
            }
        }
    }
</script>
