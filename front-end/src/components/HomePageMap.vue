<template>
  <l-map :center="center" :zoom="zoom">
    <l-tile-layer
        url="https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png"
        attribution='<a href="https://stadiamaps.com/">Stadia Maps</a>'
    ></l-tile-layer>
    <l-marker v-for="(coordinates, index) in splitCoordinates" :key="coordinates[0]" :lat-lng="coordinates" :icon="customMarkerIcon">
      <l-tooltip :options="{direction: 'bottom' }">{{ getWineryName(index) }}</l-tooltip>
    </l-marker>
  </l-map>
</template>

<script>
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'
import { LMap, LTileLayer, LMarker, LTooltip } from '@vue-leaflet/vue-leaflet'
import {store} from "@/store/store";
export default {
  name: 'StadiaMap',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
  },
  props: {
    wineries: Object,
  },
  data() {
    return {
      latitude: String,
      longitude: String,
      splitCoordinates: [],
      favorites: "",
      visited: "",
    }
  },
  computed: {
    selectedCity() {
      return store.selectedCity;
    },
    selectedRating() {
      return store.selectedRating;
    },
    favoriteClicked() {
      return store.favoriteClicked;
    },
    visitedClicked() {
      return store.visitedClicked;
    },
    customMarkerIcon() {
      return new L.Icon({
        iconUrl: require('@/assets/markerImg.png'),
        iconSize: [160, 100]
      })
    },
    filteredWineries() {
      let filtered = null;

      if(!this.selectedCity && this.selectedRating === 0) {
        filtered = this.wineries;
      }
      else if(this.selectedCity && this.selectedRating > 0) {
        filtered = this.wineries.filter(winery => winery.city.name === this.selectedCity && winery.rating >= this.selectedRating);
      }
      else if(this.selectedCity) {
        filtered = this.wineries.filter(winery => winery.city.name === this.selectedCity);
      }
      else {
        filtered = this.wineries.filter(winery => winery.rating >= this.selectedRating);
      }

      if (this.favoriteClicked) {
        filtered = filtered.filter(winery => {
          for (let favorite of this.favorites) {
            if (winery.id === favorite.id) {
              return true;
            }
          }
          return false;
        });
      }

      if (this.visitedClicked) {
        filtered = filtered.filter(winery => {
          for (let visit of this.visited) {
            if (winery.id === visit.id) {
              return true;
            }
          }
          return false;
        });
      }

      return filtered
    },
  },
  watch: {
    selectedCity: 'getCoordinates',
    selectedRating: 'getCoordinates',
    favoriteClicked: 'getCoordinates',
    visitedClicked: 'getCoordinates'
  },
  mounted() {
    this.getCoordinates();
  },
  methods: {
    getCoordinates() {
      this.getFavorites();
      this.getVisited();

      this.splitCoordinates = []

      for (let winery of this.filteredWineries) {
        if(winery["coords"]) {
          const latitude = parseFloat(winery.coords.latitude);
          const longitude = parseFloat(winery.coords.longitude);
          this.splitCoordinates.push([latitude, longitude])
        }
      }
    },
    getWineryName(index) {
      return this.filteredWineries[index].name || 'Unknown Winery';
    },
    async getFavorites() {
      const requestOptions = {
        method: "GET",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")}
      };
      const response = await fetch(store.api_url + "/profiles/favorites/", requestOptions);
      this.favorites = await response.json();

      this.favorites = JSON.parse(JSON.stringify(this.favorites))["favorites"]
    },
    async getVisited() {
      const requestOptions = {
        method: "GET",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")}
      };
      const response = await fetch(store.api_url + "/profiles/visited/", requestOptions);
      this.visited = await response.json();

      this.visited = JSON.parse(JSON.stringify(this.visited))["visited"]
    },
  }
}
</script>

<style scoped>

</style>