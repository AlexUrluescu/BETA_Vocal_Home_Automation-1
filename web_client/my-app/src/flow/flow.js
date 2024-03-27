class AppFlow {
  constructor(pathUrl) {
    this.pathUrl = pathUrl;
  }

  async getSenzorsLiveData() {
    try {
      const res = await fetch(`${url}/senzor`);
      const senzorsLiveData = await res.json();

      // MOMENTAN SENZORII NU SUNT CONECTATI
      setTempHome(senzorsLiveData.temperature);
      setHumHome(senzorsLiveData.humidity);
    } catch (error) {
      console.log(error);
    }
  }
}
