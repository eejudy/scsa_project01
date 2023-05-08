<template>
  <!-- <v-container class="container">
    <div class="card" style="width: 30rem; margin-top: 50px">
      <div class="card-body">
        <h1 class="card-text">점수</h1>
        <p style="margin-left: 10px; margin-top: 20px">{{ score }}</p>
      </div>
    </div>
    <img class="mouse-img" id="goal" :src="require('@/assets/goal.png')" />
    <v-row class="text-center" style="margin-top: 50px">
      <v-col class="mb-4">
        <div>
          <v-btn-toggle
            v-model="toggle"
            color="info"
            variant="outlined"
            style="height: 150px"
          >
            <v-btn
              @click="goal(item)"
              style="font-size: 50px; width: 200px"
              v-bind:id="`btn${item}`"
              v-for="(item, idx) in numList"
              >{{ item }}</v-btn
            >
          </v-btn-toggle>
        </div>
        <div class="buttons">
          <button @click="move" class="btn-hover color-9">닉네임 등록</button>
        </div>
      </v-col>
    </v-row>
  </v-container> -->
    <div class="body-wrapper" style="margin-top:100px;">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8 d-flex align-items-strech">
            <div>
                  <img class="mouse-img" id="goal" :src="require('@/assets/goal.png')" />
              <div class="card-body">
                <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="row">
              <div class="col-lg-12">
                <div class="card overflow-hidden">
                  <div class="card-body p-4">
                    <h5 class="card-title mb-9 fw-semibold">점수</h5>
                    <div class="row align-items-center">
                      <div class="col-8">
                        <h4 class="fw-semibold mb-3">{{score}}</h4>
                       
                        
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-12" style="margin-top:20px">
                <div class="card">
                  <div class="card-body">
                    <div class="row alig n-items-start">
                      <div class="col-8">
                        <h5 class="card-title mb-9 fw-semibold"> Monthly Earnings </h5>
                        <h4 class="fw-semibold mb-3">$6,820</h4>
                        <div class="d-flex align-items-center pb-1">
                          <span
                            class="me-2 rounded-circle bg-light-danger round-20 d-flex align-items-center justify-content-center">
                            <i class="ti ti-arrow-down-right text-danger"></i>
                          </span>
                          <p class="text-dark me-1 fs-3 mb-0">+9%</p>
                          <p class="fs-3 mb-0">last year</p>
                        </div>
                      </div>
                      <div class="col-4">
                        <div class="d-flex justify-content-end">
                          <div
                            class="text-white bg-secondary rounded-circle p-6 d-flex align-items-center justify-content-center">
                            <i class="ti ti-currency-dollar fs-6"></i>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div id="earning"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
// import $ from 'jquery'
export default {
  name: "Game",
  mounted() {},
  data: () => ({
    name: "",
    score: 0,
    numList: [1, 2, 3, 4, 5, 6],
    toggle: null,
  }),
  methods: {
    move: function () {
      //닉네임 입력 화면으로 이동
      this.$router.push("/intro");
    },
    goal(item) {
      console.log(item);
    },
  },
};
</script>

<style scoped>
.buttons {
  margin-top: 100px;
}
.soccer {
  margin-top: 340px;
  margin-right: 870px;
}
.container {
  height: 100vh;
  width: 100vw;
}
.mouse-img {
  width: 990px;
  height:490px;
  display: block;
  
}

.card {
    --bs-card-spacer-y: 30px;
    --bs-card-spacer-x: 30px;
    --bs-card-title-spacer-y: 0.5rem;
    --bs-card-title-color: #2A3547;
    --bs-card-subtitle-color: #2A3547;
    --bs-card-border-width: 0px;
    --bs-card-border-color: #ebf1f6;
    --bs-card-border-radius: 7px;
    --bs-card-box-shadow: rgba(145,158,171,0.2) 0px 0px 2px 0px,rgba(145,158,171,0.12) 0px 12px 24px -4px;
    --bs-card-inner-border-radius: 7px;
    --bs-card-cap-padding-y: 15px;
    --bs-card-cap-padding-x: 30px;
    --bs-card-cap-bg: rgba(var(--bs-body-color-rgb),0.03);
    --bs-card-cap-color: ;
    --bs-card-height: ;
    --bs-card-color: ;
    --bs-card-bg: var(--bs-body-bg);
    --bs-card-img-overlay-padding: 1rem;
    --bs-card-group-margin: 12px;
    position: relative;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    min-width: 0;
    height: var(--bs-card-height);
    word-wrap: break-word;
    background-color: var(--bs-card-bg);
    background-clip: border-box;
    border: var(--bs-card-border-width) solid var(--bs-card-border-color);
    border-radius: var(--bs-card-border-radius);
    -webkit-box-shadow: var(--bs-card-box-shadow);
    box-shadow: var(--bs-card-box-shadow)
}

.card>hr {
    margin-right: 0;
    margin-left: 0
}

.card>.list-group {
    border-top: inherit;
    border-bottom: inherit
}

.card>.list-group:first-child {
    border-top-width: 0;
    border-top-left-radius: var(--bs-card-inner-border-radius);
    border-top-right-radius: var(--bs-card-inner-border-radius)
}

.card>.list-group:last-child {
    border-bottom-width: 0;
    border-bottom-right-radius: var(--bs-card-inner-border-radius);
    border-bottom-left-radius: var(--bs-card-inner-border-radius)
}

.card>.card-header+.list-group,.card>.list-group+.card-footer {
    border-top: 0
}

.card-body {
    -webkit-box-flex: 1;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    padding: var(--bs-card-spacer-y) var(--bs-card-spacer-x);
    color: var(--bs-card-color)
}

.card-title {
    margin-bottom: var(--bs-card-title-spacer-y);
    color: var(--bs-card-title-color)
}

.card-subtitle {
    margin-top: calc(-0.5 * var(--bs-card-title-spacer-y));
    margin-bottom: 0;
    color: var(--bs-card-subtitle-color)
}

.card-text:last-child {
    margin-bottom: 0
}

.card-link+.card-link {
    margin-left: var(--bs-card-spacer-x)
}

.card-header {
    padding: var(--bs-card-cap-padding-y) var(--bs-card-cap-padding-x);
    margin-bottom: 0;
    color: var(--bs-card-cap-color);
    background-color: var(--bs-card-cap-bg);
    border-bottom: var(--bs-card-border-width) solid var(--bs-card-border-color)
}

.card-header:first-child {
    border-radius: var(--bs-card-inner-border-radius) var(--bs-card-inner-border-radius) 0 0
}

.card-footer {
    padding: var(--bs-card-cap-padding-y) var(--bs-card-cap-padding-x);
    color: var(--bs-card-cap-color);
    background-color: var(--bs-card-cap-bg);
    border-top: var(--bs-card-border-width) solid var(--bs-card-border-color)
}

.card-footer:last-child {
    border-radius: 0 0 var(--bs-card-inner-border-radius) var(--bs-card-inner-border-radius)
}

.card-header-tabs {
    margin-right: calc(-0.5 * var(--bs-card-cap-padding-x));
    margin-bottom: calc(-1 * var(--bs-card-cap-padding-y));
    margin-left: calc(-0.5 * var(--bs-card-cap-padding-x));
    border-bottom: 0
}

.card-header-tabs .nav-link.active {
    background-color: var(--bs-card-bg);
    border-bottom-color: var(--bs-card-bg)
}

.card-header-pills {
    margin-right: calc(-0.5 * var(--bs-card-cap-padding-x));
    margin-left: calc(-0.5 * var(--bs-card-cap-padding-x))
}

.card-img-overlay {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    padding: var(--bs-card-img-overlay-padding);
    border-radius: var(--bs-card-inner-border-radius)
}

.card-img,.card-img-bottom,.card-img-top {
    width: 100%
}

.card-img,.card-img-top {
    border-top-left-radius: var(--bs-card-inner-border-radius);
    border-top-right-radius: var(--bs-card-inner-border-radius)
}

.card-img,.card-img-bottom {
    border-bottom-right-radius: var(--bs-card-inner-border-radius);
    border-bottom-left-radius: var(--bs-card-inner-border-radius)
}

.card-group>.card {
    margin-bottom: var(--bs-card-group-margin)
}

@media (min-width: 576px) {
    .card-group {
        display:-webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -ms-flex-flow: row wrap;
        flex-flow: row wrap
    }

    .card-group>.card {
        -webkit-box-flex: 1;
        -ms-flex: 1 0 0%;
        flex: 1 0 0%;
        margin-bottom: 0
    }

    .card-group>.card+.card {
        margin-left: 0;
        border-left: 0
    }

    .card-group>.card:not(:last-child) {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0
    }

    .card-group>.card:not(:last-child) .card-header,.card-group>.card:not(:last-child) .card-img-top {
        border-top-right-radius: 0
    }

    .card-group>.card:not(:last-child) .card-footer,.card-group>.card:not(:last-child) .card-img-bottom {
        border-bottom-right-radius: 0
    }

    .card-group>.card:not(:first-child) {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0
    }

    .card-group>.card:not(:first-child) .card-header,.card-group>.card:not(:first-child) .card-img-top {
        border-top-left-radius: 0
    }

    .card-group>.card:not(:first-child) .card-footer,.card-group>.card:not(:first-child) .card-img-bottom {
        border-bottom-left-radius: 0
    }

}

    .col-lg-8 {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 auto;
        flex: 0 0 auto;
        width: 66.66666667%
    }

</style>
