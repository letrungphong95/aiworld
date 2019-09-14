<template>
    <div>
        <v-layout row>
            <v-flex sm2 offset-sm3 mt-2 mb-2>
                <v-btn raised class="primary" @click="onPickFile">Upload Image</v-btn>
                <input 
                    type="file" 
                    style="display:none" 
                    ref="fileInput" 
                    accept="image/*"
                    @change="onFilePicked">
            </v-flex>
            <v-flex sm2 offset-sm3 mt-2 mb-2>
                <v-btn raised class="primary" @click="predictFile">Predict</v-btn>
            </v-flex>
        </v-layout>
        <v-row align="center" justify="center">
            <v-img
                :src="imageUrl"
                aspect-ratio="1"
                class="grey lighten-2"
                max-width="500"
                max-height="300"
            ></v-img>
        </v-row>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data(){
            return {
                imageUrl: require("../assets/ironman1.jpg"),
                image: null
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
                });
                fileReader.readAsDataURL(files[0]);
                this.image = files[0]
                console.log(this.image)
                
            },
            predictFile() {
                // const fd = new FormData();
                // console.log(this.imageUrl)
                // fd.append('image_path',this.imageUrl)
                axios.post('http://127.0.0.1:8000/api/object-label', {
                    "image_path":this.image
                })
                .then(res => {
                    console.log(res)
                })
            }
        }
    }
</script>