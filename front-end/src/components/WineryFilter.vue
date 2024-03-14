<template>
  <div class="filters col-md-3 p-2">
    <div class="top d-flex justify-content-around align-items-center">
      <form @submit.prevent="selectRating">
        <div class="ratingFilter d-flex align-items-center">
          <div class="field">
            <label for="rating">Филтрирај според оцена</label>
            <input type="text" v-model="rating" id="rating" class="form-control-sm" placeholder="Внесете оцена"/>
          </div>
          <button type="submit" class="btn btn-block btn-sm">Примени</button>
        </div>
      </form>
      <div v-if="showErrorMessage" class="error-message">
        {{ this.errorMessage }}
      </div>
      <button type="submit" class="btn" @click="clearRating">✖</button>
    </div>
    <div class="bottom">
      <div class="cityFilter d-flex align-items-center">
        <h6>Филтрирај според град</h6>
        <button type="submit" class="btn" @click="clearCity">✖</button>
      </div>
      <div class="scrollbar">
        <div v-for="city in cities" :key="city.id">
          <button type="submit" class="btn btn-link" @click="selectCity(city)">{{ city.name }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mutations, store} from '../store/store.js'
export default {
  name: "WineryFilter",
  data() {
    return {
      cities: store.cities,
      rating: null,
      showErrorMessage: false,
      errorMessage: "",
    }
  },
  methods: {
    selectCity(city) {
      mutations.setSelectedCity(city.name);
    },
    selectRating() {
      if(this.rating >= 1 && this.rating <= 5) {
        mutations.setSelectedRating(this.rating);
      } else {
        this.showErrorMessage = true
        this.errorMessage = "Rating should be a value between [1,5]"
        setTimeout(() => {
          this.showErrorMessage = false;
        }, 3000);
      }
    },
    clearRating() {
      this.rating = null
      mutations.setSelectedRating(0);
    },
    clearCity() {
      mutations.setSelectedCity(null)
    }
  }
}
</script>

<style scoped>
  .field {
    display: flex;
    flex-direction: column;
  }

  .cityFilter {
    gap: 53%;
  }

  .top {
    gap: 16%;
  }

  label {
    font-weight: 500;
    line-height: 1.2;
  }

  .bottom {
    border-top: 1px solid black;
    margin-top: .5rem;
    padding-top: .5rem;
  }

  .top, .bottom {
    width: 100%;
    overflow: hidden;
  }

  .btn {
    color: var(--secondary-color);
  }

  .btn-link {
    color: black;
    text-decoration: none;
  }

  .btn-link:hover {
    color: var(--primary-color);
  }

  .btn-sm {
    height: 10%;
    margin-left: .5rem;
    background-color: var(--primary-color);
    color: white;
  }

  .btn-sm:hover {
    background-color: var(--secondary-color);
    border: 1px solid var(--primary-color);
    color: var(--primary-color);
  }

  .form-control-sm {
    border: 1px solid lightgrey;
  }

  .scrollbar {
    height: 63vh;
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .scrollbar::-webkit-scrollbar {
    width: .8rem;
  }

  .scrollbar::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: var(--secondary-color);
    border: 1px solid #cacaca;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  .scrollbar::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: var(--primary-color);
  }

  .error-message {
    position: fixed;
    top: 82px;
    left: 10.5%;
    transform: translateX(-50%);
    background-color: var(--primary-color);
    color: white;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
</style>