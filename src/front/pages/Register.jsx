import {useState} from "react"
import useGlobalReducer from "../hooks/useGlobalReducer"
import {Link, useNavigate} from "react-router-dom"

const initialStateRegister = {
    full_name: '',
    email: '',
    phone_number: '',
    password: '',
    // farm_name: '',
    // farm_location: '',
    avatar: '',
    acceptTerms: false,
}

export const Register = () => {

    const {distpach, store} = useGlobalReducer()

    const navigate = useNavigate()

    const [formData, setFormData] = useState(initialStateRegister);    // es lo que voy a mandar en el body

    const [showPassword, setShowPassword] = useState(false);
    
    const [isLoading, setIsLoading] = useState(false);

    const handleInputChange = (event) => {
        const { name, value, type, checked } = event.target;
        setFormData((formData) => ({
            ...formData,
            [name]: type === 'checkbox' ? checked : value
        }));
    };

    const handleSubmit = async (event) => {     // asegurarme que el handleInputChange (controla el imput y envia eventos) mande todo bien a formdata 
        event.preventDefault()
        console.log("hola soy el boton de submit")
        const urlBackend = import.meta.env.VITE_BACKEND_URL;

        const response = await fetch(`${urlBackend}/register`, {
            method: "POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })

        if (response.status === 201) {
            setFormData(initialStateRegister)
            setTimeout(() => {
                navigate("/login")
            }, 2000)
        } else if (response.status === 400) {
            alert("El usuario ya existe")
        } else {
            alert("Error al registrar el usuario, intente nuevamente")
        }

        if (!formData.acceptTerms) {
            alert('Debes aceptar los términos y condiciones');
            return;
        }

        setIsLoading(true);
        setTimeout(() => {
            setIsLoading(false);
            alert('Registrar');
        }, 2000);
    }

    return (
        <div className="min-vh-100 d-flex align-items-center bg-light">
            <div className="container py-5">
                <div className="row justify-content-center">
                    <div className="col-md-6 col-lg-5">
                        <div className="card shadow-sm border-0 rounded-4">
                            <div className="card-body p-4">
                                {/* Logo y título */}
                                <div className="text-center mb-4">
                                    <i className="fas fa-leaf fa-2x text-success mb-2"></i>
                                    <h1 className="h4 fw-bold text-dark">AgriVision AI</h1>
                                </div>

                                <h2 className="h5 text-center text-dark mb-4">Crear Cuenta</h2>

                                <form onSubmit={handleSubmit}>
                                    {/* Nombre */}
                                    <div className="mb-3">
                                        <label htmlFor="fullName" className="form-label">Nombre Completo</label>
                                        <div className="input-group">
                                            <input
                                                type="text"
                                                className="form-control"
                                                id="fullName"
                                                placeholder="Ingresa tu nombre"
                                                name="full_name"
                                                value={formData.full_name}
                                                onChange={handleInputChange}
                                                required
                                            />
                                        </div>
                                        <div className="invalid-feedback">
                                            Este campo es obligatorio.
                                        </div>
                                    </div>

                                    {/* Teléfono */}
                                    <div className="mb-3">
                                        <label htmlFor="phone" className="form-label">Teléfono</label>
                                        <div className="input-group">
                                            <input
                                                type="number"
                                                className="form-control"
                                                id="phone"
                                                placeholder="56 9 1234 5678"
                                                name="phone_number"
                                                value={formData.phone_number}
                                                onChange={handleInputChange}
                                                required
                                            />
                                        </div>
                                        <div className="invalid-feedback">
                                            Este campo es obligatorio.
                                        </div>
                                    </div>

                                    {/* Nombre del Huerto */}
                                    {/*<div className="mb-3">
                                        <label htmlFor="farmName" className="form-label">Nombre del Campo</label>
                                        <div className="input-group">
                                            <input
                                                type="text"
                                                className="form-control"
                                                id="farmName"
                                                placeholder="Nombre del campo"
                                                name="farm_name"
                                                value={formData.farm_name}
                                                onChange={handleInputChange}
                                                required
                                            />
                                        </div>
                                        <div className="invalid-feedback">
                                            Este campo es obligatorio.
                                        </div>
                                    </div>*/}

                                    {/* Ubicación del Huerto */}
                                    {/*<div className="mb-3">
                                        <label htmlFor="farmLocation" className="form-label">Ubicación del Campo</label>
                                        <div className="input-group">
                                            <input
                                                type="text"
                                                className="form-control"
                                                id="farmLocation"
                                                placeholder="Ubicación del campo"
                                                name="farm_location"
                                                value={formData.farm_location}
                                                onChange={handleInputChange}
                                                required
                                            />
                                        </div>
                                        <div className="invalid-feedback">
                                            Este campo es obligatorio.
                                        </div>
                                    </div>*/}

                                    {/* Avatar */}

                                    <div className="form-group mb-3 ">
                                        <label htmlFor="btnAvatar" className="form-label">Imágen de Perfil:</label>
                                        <input
                                            type="file"
                                            className="form-control border-0"
                                            id="btnAvatar"
                                            placeholder="Cargar Imágen"
                                            name="avatar"
                                            onChange={handleInputChange}
                                            value={formData.avatar}
                                        />
                                    </div>

                                    {/* Correo */}
                                    <div className="mb-3">
                                        <label htmlFor="email" className="form-label">Correo electrónico</label>
                                        <div className="input-group">
                                            <span className="input-group-text">
                                                <i className="fas fa-envelope text-secondary"></i>
                                            </span>
                                            <input
                                                type="email"
                                                className="form-control"
                                                id="email"
                                                placeholder="Ingresa tu correo"
                                                name="email"
                                                value={formData.email}
                                                onChange={handleInputChange}
                                                required
                                            />
                                        </div>
                                        <div className="invalid-feedback">
                                            Este campo es obligatorio.
                                        </div>
                                    </div>

                                    {/* Contraseña */}
                                    <div className="mb-3">
                                        <label htmlFor="password" className="form-label">Contraseña</label>
                                        <div className="input-group">
                                            <span className="input-group-text">
                                                <i className="fas fa-lock text-secondary"></i>
                                            </span>
                                            <input
                                                type={showPassword ? 'text' : 'password'}
                                                className="form-control"
                                                id="password"
                                                placeholder="Ingresa tu contraseña"
                                                name="password"
                                                value={formData.password}
                                                onChange={handleInputChange}
                                                required
                                            />
                                            <button
                                                type="button"
                                                className="btn btn-outline-secondary"
                                                onClick={() => setShowPassword(!showPassword)}
                                                tabIndex={-1}
                                            >
                                                <i className={`fas ${showPassword ? 'fa-eye-slash' : 'fa-eye'}`}></i>
                                            </button>
                                        </div>
                                        <div className="invalid-feedback">
                                            Este campo es obligatorio.
                                        </div>
                                    </div>

                                    {/* Aceptación de términos */}
                                    <div className="mb-3">
                                        <div className="form-check">
                                            <input className="form-check-input" type="checkbox" value="" id="invalidCheck" required/>
                                            <label className="form-check-label" htmlFor="invalidCheck">
                                                Acepto los términos y condiciones.
                                            </label>
                                            <div className="invalid-feedback">
                                                You must agree before submitting.
                                            </div>
                                        </div>
                                    </div>

                                    {/* Botón */}
                                    <button
                                        type="submit"
                                        className="btn btn-success w-100"
                                        disabled={isLoading}
                                        onClick={() => setFormData()}
                                    >
                                        {isLoading ? 'Creando cuenta...' : 'Crear cuenta'}
                                    </button>
                                </form>

                                <div className="text-center mt-4">
                                    <p className="small text-muted">
                                        ¿Ya tienes una cuenta?{' '}
                                        <Link to="/login" className="text-success fw-semibold text-decoration-none">
                                            Inicia sesión
                                        </Link>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

