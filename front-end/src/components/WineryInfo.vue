<template>
  <div class="left1">
    <div class="d-flex justify-content-start align-items-center gap-5">
      <div class="d-flex align-items-center justify-content-start gap-3">
        <h2>{{ selectedWinery.name }}</h2>
        <i class="visitedLocation fas fa-map-marker-alt" @click="clickedVisited" :class="{'active': isVisited, 'hide' : !userLoggedIn}"></i>
        <i class="heart fas fa-heart" @click="clickedFavorite" :class="{'active': isFavorite, 'hide' : !userLoggedIn}"></i>
      </div>
      <div class="d-flex align-items-center">
        <i class="fas fa-star mx-2 fa-xs"></i>
        <p v-if="selectedWinery.rating!=null" class="mb-0">{{ selectedWinery.rating }}</p>
        <p v-else class="mb-0">No Info</p>
      </div>
    </div>
    <h3 v-if="selectedWinery.city">{{ selectedWinery.city.name }}</h3>
    <h4 v-if="selectedWinery.address">{{ selectedWinery.address }}</h4>
    <h5 v-if="selectedWinery.work">{{ selectedWinery.work }}</h5>
    <h5 v-if="selectedWinery.phone">{{ selectedWinery.phone }}</h5>
  </div>
</template>

<script>
import { store } from '@/store/store.js'
export default {
  name: "WineryInfo",
  data() {
    return {
      isFavorite: false,
      isVisited: false,
    }
  },
  computed: {
    userLoggedIn() {
      return sessionStorage.getItem("loggedIn") === "true"
    },
    selectedWinery() {
      const storedWinery = sessionStorage.getItem("selectedWinery");
      return JSON.parse(storedWinery);
    }
  },
  created() {
    this.initializeFavoriteStatus();
    this.initializeVisitedStatus()
  },
  methods: {
    async clickedFavorite() {
      this.isFavorite = !this.isFavorite;
      sessionStorage.setItem(`isFavorite_${this.selectedWinery.id}`, JSON.stringify(this.isFavorite));

      if(this.isFavorite) {
        this.addToFavorites();
      } else {
        this.removeFromFavorites();
      }
    },

    async addToFavorites() {
      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
        body: JSON.stringify({"winery_id":this.selectedWinery.id})
      };
      await fetch(store.api_url + "/profiles/favorites/", requestOptions);
    },

    async removeFromFavorites() {
      const requestOptions = {
        method: "DELETE",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
        body: JSON.stringify({"winery_id":this.selectedWinery.id})
      };
      await fetch(store.api_url + "/profiles/favorites/", requestOptions);
    },

    async clickedVisited() {
      this.isVisited = !this.isVisited;
      sessionStorage.setItem(`isVisited_${this.selectedWinery.id}`, JSON.stringify(this.isVisited));

      if(this.isVisited) {
        this.addToVisited();
      } else {
        this.removeFromVisited();
      }
    },

    async addToVisited() {
      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
        body: JSON.stringify({"winery_id":this.selectedWinery.id})
      };
      await fetch(store.api_url + "/profiles/visited/", requestOptions);
    },

    async removeFromVisited() {
      const requestOptions = {
        method: "DELETE",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
        body: JSON.stringify({"winery_id":this.selectedWinery.id})
      };
      await fetch(store.api_url + "/profiles/visited/", requestOptions);
    },

    async initializeFavoriteStatus() {
      if(this.userLoggedIn) {
        const storedIsFavorite = sessionStorage.getItem(`isFavorite_${this.selectedWinery.id}`);

        if(storedIsFavorite !== null) {
          this.isFavorite = JSON.parse(storedIsFavorite)
        } else {
          const requestOptions = {
            method: "GET",
            headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")}
          };
          const response = await fetch(store.api_url + "/profiles/favorites/", requestOptions);
          let favorites = await response.json();
          favorites = JSON.parse(JSON.stringify(favorites))["favorites"]

          this.isFavorite = favorites.includes(this.selectedWinery.id);
          sessionStorage.setItem(`isFavorite_${this.selectedWinery.id}`, JSON.stringify(this.isFavorite));
        }
      }
    },
    async initializeVisitedStatus() {
      if(this.userLoggedIn) {
        const storedIsVisited = sessionStorage.getItem(`isVisited_${this.selectedWinery.id}`);

        if(storedIsVisited !== null) {
          this.isVisited = JSON.parse(storedIsVisited)
        } else {
          const requestOptions = {
            method: "GET",
            headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")}
          };
          const response = await fetch(store.api_url + "/profiles/visited/", requestOptions);
          let visited = await response.json();
          visited = JSON.parse(JSON.stringify(visited))["visited"]

          this.isVisited = visited.includes(this.selectedWinery.id);
          sessionStorage.setItem(`isVisited_${this.selectedWinery.id}`, JSON.stringify(this.isVisited));
        }
      }
    },
  }
}
</script>

<style scoped>
  .left1 {
    padding-top: 2rem;
    height: 18rem;
  }

  .heart, .visitedLocation {
    font-size: 25px;
    color: darkgray;
  }

  .fa-star {
    font-size: 25px;
    color: var(--accent-color);
  }

  .active {
    font-size: 25px;
    color: var(--primary-color);
  }

  .hide {
    visibility: hidden;
  }
</style>