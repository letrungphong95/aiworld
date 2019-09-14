<template>
  <div>
    <v-content>
      <section>
        <v-parallax src="../assets/ironman1.jpg" height="500">
          <v-layout
            column
            align-center
            justify-center
            class="white--text"
          >
            <!-- <img src="../assets/phong.jpeg" alt="Vuetify.js" height="200" style="border-radius: 50%"> -->
            <img width="120" height="120" class="avatar" alt="sample-image" src="../assets/phong.jpeg">
            <h1 class="white--text display-1 text-center">Welcome to AI World</h1>
            <div class="subheading text-center">
                <v-flex sm4 offset-sm4 class="my-4">
                    <div class="text-center">
                        <p>I am just an AI enthusiast. I love working with machine, so I work as an AI Engineer. 
                        Futhermore, I also have experience of working with web developing.
                        Now, I want to have a chance to share my knowledge about AI, Web.
                        My next goal is to be a Magical Dev to 🔥the world.</p>
                    </div>
                </v-flex>
            </div>
            <router-link 
            to="/demo"
            style="text-decoration: none;">
              <v-btn
                color="blue lighten-2"
                dark
                large
              >
                Get Started with Demo
              </v-btn>
            </router-link>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-layout
          column
          wrap
          class="my-12"
          align-center
        >
        <div>
          <v-flex sm10 offset-sm1 class="my-4">
          <!-- <v-flex xs12 sm4 class="my-4"> -->
            <div class="text-center">
              <!-- <h2 class="headline">The best way to start learning AI from scratch</h2> -->
              <h2 class="display-1 font-weight-light">What is the best way to learn AI from scratch?</h2>
              <span class="subheading display-1 font-weight-light">
                The answer is you need to love it first.
              </span>
            </div>
          

            <v-timeline :dense="$vuetify.breakpoint.smAndDown">
                <v-timeline-item
                color="purple lighten-2"
                fill-dot
                right
                >
                <v-card>
                    <v-card-title class="purple lighten-2">
                    <v-icon
                        dark
                        size="42"
                        class="mr-4"
                    >
                        mdi-magnify
                    </v-icon>
                    <h3 class="white--text font-weight-light">Choose correct way to learn</h3>
                    </v-card-title>
                    <v-container>
                    <v-row>
                        <v-col cols="12" md="12">
                        if you are reading this lines, yeah congrat to you because of choosing exact method to learn AI.
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
                </v-timeline-item>

                <v-timeline-item
                color="amber lighten-1"
                fill-dot
                left
                small
                >
                <v-card>
                    <v-card-title class="amber lighten-1 justify-end">
                    <h3 class="mr-4 white--text font-weight-light">Understand about what AI is</h3>
                    <v-icon
                        dark
                        size="42"
                    >mdi-home-outline</v-icon>
                    </v-card-title>
                    <v-container>
                    <v-row>
                        <v-col cols="12" md="12">
                        For simple understanding, AI is just the simulation of human brain which is processed on computer.
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
                </v-timeline-item>

                <v-timeline-item
                color="cyan lighten-1"
                fill-dot
                right
                >
                <v-card>
                    <v-card-title class="cyan lighten-1">
                    <v-icon
                        class="mr-4"
                        dark
                        size="42"
                    >
                        mdi-eye
                    </v-icon>
                    <h3 class="white--text font-weight-light">Computer Vision</h3>
                    </v-card-title>
                    <v-container>
                    <v-row>
                        <v-col cols="12" md="12">
                        Computer Vision is one of major parts of AI. If AI is the simulation of human brain,  Computer Vision is the simulation of human eyes.
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
                </v-timeline-item>

                <v-timeline-item
                color="red lighten-1"
                fill-dot
                left
                small
                >
                <v-card>
                    <v-card-title class="red lighten-1 justify-end">
                    <h3 class="mr-4 white--text font-weight-light">Natural Language Processing</h3>
                    <v-icon
                        dark
                        size="42"
                    >
                        mdi-text-to-speech
                    </v-icon>
                    </v-card-title>
                    <v-container>
                    <v-row>
                        <v-col cols="12" md="12">
                        Another major part of AI is NLP (Natual Language Processing). NLP will be the simulation of human ear and human mouth.
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
                </v-timeline-item>

                <v-timeline-item
                color="green lighten-1"
                fill-dot
                right
                >
                <v-card>
                    <v-card-title class="green lighten-1">
                    <v-icon
                        class="mr-4"
                        dark
                        size="42"
                    >
                        mdi-weather-cloudy
                    </v-icon>
                    <h3 class="white--text font-weight-light">Production</h3>
                    </v-card-title>
                    <v-container>
                    <v-row>
                        <v-col cols="12" md="12">
                        After finishing this AI course, you can implement several simple AI applications by yourself. Then you will be supported to deploy it on web, app... to share for everyone who need it.
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
                </v-timeline-item>
            </v-timeline>
            </v-flex>
          </div>
        </v-layout>
      </section>

      <section>
        <v-carousel cycle>
          <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
          ></v-carousel-item>
        </v-carousel>
      </section>

      <section>
        <v-container grid-list-xl>
          <v-layout row wrap justify-center class="my-12">
            <v-flex mb-10 xs12 sm4 offset-sm1>
              <v-card flat class="transparent">
                <v-card-title class="text-center">
                  <div class="headline">Good luck and have a good day!</div>
                </v-card-title>
                <v-card-text>
                  "Live as if you were to die tomorrow, learn as if you were to live forever."
                </v-card-text>
                <v-list class="transparent">
                  <v-list-item>
                    <v-list-item-action>
                      <v-icon class="blue--text text--lighten-2">mdi-phone</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>01206215650</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-action>
                      <v-icon class="blue--text text--lighten-2">mdi-map-marker</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>Da Nang, Viet Nam</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-action>
                      <v-icon class="blue--text text--lighten-2">mdi-email</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>letrungphong95@gmail.com</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </section>
    </v-content>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          {
            src: require('../assets/slide1.jpg'),
          },
          {
            src: require('../assets/slide2.jpg'),
          },
          {
            src: require('../assets/slide3.png'),
          },
          {
            src: require('../assets/slide4.jpg'),
          },
          {
            src: require('../assets/slide5.jpg'),
          }
        ],
      }
    },
  }
</script>

<style scoped>
    .avatar {
        /* width: 60%; */
        scale: 60%;
        border-radius: 50%;
        height: 214px;
        width: 214px;
        object-fit: cover;
    }
</style>