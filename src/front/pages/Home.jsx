import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";

export const Home = () => {

	// const { store, dispatch } = useGlobalReducer()

	// const loadMessage = async () => {
	// 	try {
	// 		const backendUrl = import.meta.env.VITE_BACKEND_URL

	// 		if (!backendUrl) throw new Error("VITE_BACKEND_URL is not defined in .env file")

	// 		const response = await fetch(backendUrl + "/api/hello")
	// 		const data = await response.json()

	// 		if (response.ok) dispatch({ type: "set_hello", payload: data.message })

	// 		return data

	// 	} catch (error) {
	// 		if (error.message) throw new Error(
	// 			`Could not fetch the message from the backend.
	// 			Please check if the backend is running and the backend port is public.`
	// 		);
	// 	}

	// }

	// useEffect(() => {
	// 	loadMessage()
	// }, [])

	return (

		<div>
			{/* contenedor 1 */}
			<div className="bg-green-gradient p-5">
				{/* sub contenedor 1 */}
				<div className="text-center pb-3">
					<h1><span className="fw-bold text-dark fs-8 px-2">AgriVision AI</span></h1>
				</div>
				{/* sub contenedor 2 */}
				<div className="fw-bold text-center pb-3">
					<h1>Transforma tu agricultura con</h1>
					<h1>Inteligencia Artificial</h1>
				</div>
				{/* sub contenedor 3 */}
				<div>
					<p className = "text-center">
						Sube imágenes de drones y obtén análisis instantáneos sobre la salud de tus cultivos, estrés hídrico, niveles de nutrientes y recomendaciones precisas para optimizar tu cosecha.
					</p>
				</div>
				{/* sub contenedor 4 */}
				<div className="d-flex justify-content-center align-content-center g-5">
					<button className="rounded-3 btn btn-succes bg-success text-white fw-bold border border-success-subtle">comenzar analisis gratuito</button>
					<button className="rounded-3 btn btn-white border fw-bold border-secondary-subtle"><i>flecha reproduccion</i>Ver Demo</button>
				</div>
				{/* sub contenedor 5 */}
				<div className="d-flex justify-content-between align-content-center">
					<button className="rounded-5 btn btn-white fw-bold border border-secondary-subtle"><i>nube con sol</i>Análisis en Tiempo Real</button>
					<button className="rounded-5 btn btn-white fw-bold border border-secondary-subtle"><i>brote emergiendo</i>Monitoreo de Salud</button>
					<button className="rounded-5 btn btn-white fw-bold border border-secondary-subtle"><i>gota</i>Detección de Estrés Hídrico</button>
				</div>
			</div>

			<div className="mx-5">
				{/* contenedor 2 */}
				<div className="text-center my-5">
					<h2 >Sube tus Imágenes Aéreas</h2>
					<p classname = "mx-4">
						Obtén análisis instantáneos impulsados por IA sobre la salud de tus cultivos y las condiciones de crecimiento
					</p>
				</div>
				{/* contenedor 3 */}
				<div className="border rounded-4 shadow">
					<div className="d-flex justify-content-start align-content-center">
						<span className = "d-flex m-4">
							<i>camara</i><h3>Subir Imagen Aérea</h3>
						</span>
					</div>
					<div className="border rounded-4 text-center p-5 m-4 mb-5">
						Agregar imagen
					</div>
				</div>
				{/* contenedor 4 */}
				<div className="text-center my-5 py-5 border rounded-4 shadow">
					<i>sol</i>
					<h3>Resultados del Análisis</h3>
					<p>
						Sube una imagen para ver el análisis detallado del cultivo
					</p>
				</div>
				{/* contenedor 5 */}
				<div>
					<div className="container">
						

						<div className="row g-3">
							<div className="col-12 text-center mt-5 ">
								<h1>¿Por qué elegir AgriVision AI?</h1>
								<p>
									Nuestra plataforma combina tecnología IA de vanguardia con experiencia agrícola para ayudarte a tomar decisiones basadas en datos.
								</p>
							</div>

							<div className="col-6 text-center mt-5 border rounded-4 shadow">
								<i>imagen</i>
								<h3>Análisis Multi-Fuente</h3>
								<p>
									Soporte para imágenes de drones, datos satelitales y fotografía terrestre para un análisis integral del campo.
								</p>
							</div>

							<div className="col-6 text-center mt-5 border rounded-4 shadow">
								<i>lupa</i>
								<h3>IA Avanzada</h3>
								<p>
									Algoritmos de aprendizaje automático detectan estrés en cultivos, enfermedades y patrones de crecimiento con alta precisión.
								</p>
							</div>

							<div className="col-6 text-center mt-5 border rounded-4 shadow">
								<i>hoja</i>
								<h3>Recomendaciones Precisas</h3>
								<p>
									Obtén recomendaciones específicas y accionables para estrategias de riego, fertilización y manejo de plagas.
								</p>
							</div>

							<div className="col-6 text-center mt-5 border rounded-4 shadow">
								<i>flecha tendencia</i>
								<h3>Análisis de Tendencias</h3>
								<p>
									Monitorea el progreso de tus cultivos a lo largo del tiempo con reportes detallados y análisis comparativos.
								</p>
							</div>

							<div className="col-6 text-center mt-5 border rounded-4 shadow">
								<i>escudo</i>
								<h3>Detección Temprana</h3>
								<p>
									Identifica problemas antes de que se vuelvan críticos, ahorrando tiempo y recursos valiosos.
								</p>
							</div>

							<div className="col-6 text-center mt-5 border rounded-4 shadow">
								<i>rayo</i>
								<h3>Resultados Instantáneos</h3>
								<p>
									Obtén análisis completos en segundos, no en días. Toma decisiones informadas al instante.
								</p>
							</div>

							<div className="col-12 text-center mt-5 border rounded-4">
								<h1></h1>
								<p>
									Sube una imagen para ver el análisis detallado del cultivo
								</p>
								<button>
									Comenzar prueba gratis
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

	);
}; 