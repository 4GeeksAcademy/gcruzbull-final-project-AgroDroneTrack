import {useState} from "react"
import useGlobalReducer from "../hooks/useGlobalReducer"
import {Link, useNavigate} from "react-router-dom"
import { Register } from "./Register"

// const initialStateRegister = {
//     fullName: '',
//     phoneNumber: '',
//     email:'',
//     farm_name: '',
//     farm_location: '',
//     avatar: '',
// }

export const Profile = () => {

    const {distpach, store} = useGlobalReducer()

    const navigate = useNavigate()

    // const [clientData, setClientData] = useState(initialStateRegister);
    
    const [isLoading, setIsLoading] = useState(false);

    const profileData = async () => {

        const urlBackend = import.meta.env.VITE_BACKEND_URL;

        const response = await fetch(`${urlBackend}/profile`, {
            method: "POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user)
        })

        // setIsLoading(true);
        // setTimeout(() => {
        //     setIsLoading(false);
        //     alert('');
        // }, 2000);
    }

    return (
        
            <div className="container py-5">
                <h2 className="mb-4">Perfil</h2>
                <div className="row">
                    {/* Avatar */}
                    <div className="col-md-4">
                        <img src={Register.avatar} alt="" />   
                    </div>

                    {/* Datos personales */}
                    <div className="col-md-8">
                        {/* Parte texto */}
                        <div className="">
                            <div className="card-body">
                                <div>
                                    <p className="mb-1 fw-bold">Nombre:</p>
                                    <p>
                                        {Register.fullName}    
                                    </p>
                                </div>

                                <div>
                                    <p className="fw-bold mb-1">Email:</p>
                                    <p>{Register.email}</p>
                                </div>

                                <div>
                                    <p className="fw-bold mb-1">Teléfono:</p>
                                    <p>{Register.phoneNumber}</p>
                                </div>
                                        
                                <div>
                                    <p className="fw-bold mb-1">Hubicación del huerto:</p>
                                    <p>{Register.farm_location}</p>
                                </div>

                                <div>
                                    <p className="fw-bold mb-1">Nombre del huerto:</p>
                                    <p>{Register.farm_name}</p>
                                </div>
                            </div> 
                        </div>
                    </div>

                    {/* botones */}

                    <div className="col-md-12">
                        <ul className="list-unstyled">
                            <li className="my-2">
                                <button
                                    type="submit"
                                    className="btn btn-success "
                                    disabled= {true}
                                >
                                    <Link className="text-white text-decoration-none">
                                        Registro Fitosanitario
                                    </Link>
                                </button>
                            </li>

                            <li className="my-2">
                                <button
                                    type="submit"
                                    className="btn btn-success "
                                    disabled= {true}
                                >
                                    <Link className="text-white text-decoration-none">
                                        Registro Nutricional
                                    </Link>
                                </button>
                            </li>

                            {/* <li className="my-2">
                                <button
                                    type="submit"
                                    className="btn btn-success "
                                    disabled= {true}
                                >
                                    <Link className="text-white text-decoration-none">
                                        Registro Climatico
                                    </Link>
                                </button>
                            </li> */}

                            <li className="my-2">
                                <button
                                    type="submit"
                                    className="btn btn-success "
                                    disabled= {true}
                                >
                                    <Link className="text-white text-decoration-none">
                                        Mapa del Huerto
                                    </Link>
                                </button>
                            </li>

                            {/* <li className="my-2">
                                <button
                                    type="submit"
                                    className="btn btn-success "
                                    disabled= {true}
                                >
                                    <Link className="text-white text-decoration-none">
                                        Gráficos
                                    </Link>
                                </button>
                            </li> */}
                        </ul>

                    </div>
                </div>
            </div>
       
    )
};
